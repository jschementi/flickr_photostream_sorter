from datetime import datetime
from os import environ
from os.path import expanduser, join
import json

import flickrapi

home = expanduser("~")

flickr_key = environ['FLICKR_API_KEY']
flickr_secret = environ['FLICKR_SECRET']

def main():

    flickr = flickrapi.FlickrAPI(flickr_key, flickr_secret, format='json')

    (token, frob) = flickr.get_token_part_one(perms='write')

    if not token:
        raw_input("Press ENTER after you authorized this program")
        token = flickr.get_token_part_two((token, frob))

    all_photos = []

    try:
        with open(join(home, ".flickr/photos.json"), "r") as photos_file:
            print '-----> Using cached photos'
            all_photos = json.loads(photos_file.read())
    except IOError:
        print '-----> Fetching all photos'
        total_pages = 1
        page = 1
        while page <= total_pages:
            print '       Fetching page {} out of {}'.format(page, total_pages)
            res = json.loads(flickr.photos_search(user_id='me', page=page, per_page=500, extras='date_upload,date_taken')[14:-1])
            total_pages = res['photos']['pages']
            page = res['photos']['page'] + 1
            photos = res['photos']['photo']
            all_photos.extend(photos)
        with open(join(home, '.flickr/photos.json'), 'w') as photos_file:
            print '-----> Saving photos for future use'
            photos_file.write(json.dumps(all_photos))

    print '-----> Updating dates'

    for photo in  all_photos:
        date_taken = photo['datetaken']
        date_taken = datetime.strptime(date_taken, '%Y-%m-%d %H:%M:%S')
        date_posted = int(photo['dateupload'])
        date_posted = datetime.fromtimestamp(date_posted)
        if date_posted != date_taken:
            print '       Updating "{}": change date posted from {} to {}'.format(photo['id'], date_posted, date_taken)
            new_date_posted = datetime.strftime(date_taken, '%s')
            flickr.photos_setDates(photo_id=photo['id'], date_posted=new_date_posted)
        else:
            print '       Skipping "{}": dates match'.format(photo['id'])

    print '-----> Done!'

if __name__ == "__main__":
    main()
