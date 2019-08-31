def recite(start_verse, end_verse):
    days={1:"On the first day of Christmas my true love gave to me",2:"On the second day of Christmas my true love gave to me",3:"On the third day of Christmas my true love gave to me",4:"On the fourth day of Christmas my true love gave to me",5:"On the fifth day of Christmas my true love gave to me",6:"On the sixth day of Christmas my true love gave to me",7:"On the seventh day of Christmas my true love gave to me",8:"On the eighth day of Christmas my true love gave to me",9:"On the ninth day of Christmas my true love gave to me",10:"On the tenth day of Christmas my true love gave to me",11:"On the eleventh day of Christmas my true love gave to me",12:"On the twelfth day of Christmas my true love gave to me"}

    items={1:"a Partridge in a Pear Tree.",2:"two Turtle Doves, and a Partridge in a Pear Tree.",3:"three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",4:"four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",5:"five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",6:"six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",7:"seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",8:"eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",9:"nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",10:"ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",11:"eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.",12:"twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."}
    expected=[]
    for verse in range(start_verse,end_verse+1):
        item=items[verse]
        expected.append(days[verse]+':'+' '+items[verse])
    return expected
##########################################################################################################################################
#Output the lyrics to 'The Twelve Days of Christmas'.
#
#On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.
#
#On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.
#
#On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
#
#On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a #Pear Tree.
#
#On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a #Partridge in a Pear Tree.
#
#On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two #Turtle Doves, and a Partridge in a Pear Tree.
#
#On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling #Birds, three French Hens, two Turtle Doves, and a Partrid#ge in a Pear Tree.
#
#On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold #Rings, four Calling Birds, three French Hens, two Turtl#e Doves, and a Partridge in a Pear Tree.
#
#On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six #Geese-a-Laying, five Gold Rings, four Calling Birds, three Fr#ench Hens, two Turtle Doves, and a Partridge in a Pear Tree.
#
#On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven #Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Ca#lling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear #Tree.
#
#On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight #Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying##, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, #and a Partridge in a Pear Tree.
#
#On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine #Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French #Hens, two Turtle Doves, and a Partridge in a Pear Tree.
#############################################################################################################################
