from pylab import *

image = ( imread( "cars1_01.png" ) * 255 ).astype( uint8 )

b = image.view( dtype="u1, u1, u1" )

un = unique( b )

print un

imshow( ( b == un[ 0 ] ).reshape( 480, 640 ) )
show()

ma = ( b == un[ 0 ] ).reshape( 480, 640 ).nonzero()

print ma[ 0 ]
print ma[ 1 ]

imshow( image )
show()