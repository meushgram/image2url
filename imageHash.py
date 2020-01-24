from PIL import Image
import imagehash
hash = imagehash.average_hash(Image.open('/Users/dhanushkumar/Desktop/Screenshot 2020-01-20 at 12.34.48 PM.png'))
print(' Hash is + {}'.format(hash))
otherhash = imagehash.average_hash(Image.open('/Users/dhanushkumar/Desktop/Screenshot 2020-01-20 at 10.53.47 AM.png'))
print(' Hash is + {}'.format(otherhash))
#test