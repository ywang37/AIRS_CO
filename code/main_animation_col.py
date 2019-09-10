"""
Created on September 9, 2019

@author: Yi Wang
"""

import datetime
import matplotlib.animation as animation
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


#######################
# Start user parameters
#

# Starting date
start_date = '2017-08-01'

# Ending date
end_date = '2017-09-30'

varnames = ['TotCO_A', 'TotCO_D']
#varnames = ['CO_VMR_A', ]

# figure directory
fig_dir = '/Dedicated/jwang-data/ywang/Jun/AIRS_CO/figure/'

#
# End user parameters
#####################

for varn in varnames:

    img_list = []
    fig = plt.figure(figsize=(8,5))
    plt.subplots_adjust(bottom=0.0, top=1.0, left=0.0, right=1.0)

    # loop date
    curr_date   = start_date
    curr_date_d = datetime.datetime.strptime(curr_date, '%Y-%m-%d')
    end_date_d  = datetime.datetime.strptime(end_date,  '%Y-%m-%d')
    while curr_date_d <= end_date_d:

        # current date
        curr_date = str(curr_date_d)[0:10]
        print('--------------------- ' + curr_date +
              ' ---------------------')
            
        # read image
        imgname = fig_dir + varn + '_' + curr_date + '.png'
        print('read ' + imgname)
        img = mpimg.imread(imgname)
        img_list.append([plt.imshow(img, animated=True)])

        # go to next day
        curr_date_d = curr_date_d + datetime.timedelta(days=1)

    ani = animation.ArtistAnimation(fig, img_list, interval=600,
            blit=True, repeat_delay=20000)
    out_file = fig_dir + varn + '_' + start_date + '_' + end_date + '.gif'
    ani.save(out_file, dpi=300)

