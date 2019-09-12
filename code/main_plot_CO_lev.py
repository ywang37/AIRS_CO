"""
Created on September 9, 2019

@author: Yi Wang
"""

import datetime
import glob

from mylib.plot_airs import plot_AIRS3STD_lev

#######################
# Start user parameters
#

# Starting date
start_date = '2017-08-01'

# Ending date
end_date = '2017-09-30'

varnames = ['CO_VMR_A', 'CO_VMR_D']

vmin = {
        'CO_VMR_A': 0.0,
        'CO_VMR_D': 0.0,
        }
vmax = {
        'CO_VMR_A': 200.0,
        'CO_VMR_D': 200.0,
        }

scale = {
        'CO_VMR_A': 1e9,
        'CO_VMR_D': 1e9,
        }

cbar_label = {
        'CO_VMR_A': 'CO [ppbv]',
        'CO_VMR_D': 'CO [ppbv]',
        }

title = {
        'CO_VMR_A': 'CO concentration (ascending orbit)',
        'CO_VMR_D': 'CO concentration (ascending orbit)',
        }

# pressure levels [hPa]
levels = [500.0]

# file directory
file_dir = '/Dedicated/jwang-data/shared_satData/AIRS_L3/AIRS3STD/2017/'

# figure directory
fig_dir = '/Dedicated/jwang-data/ywang/Jun/AIRS_CO/figure/'

#
# End user parameters
#####################


# loop date
curr_date   = start_date
curr_date_d = datetime.datetime.strptime(curr_date, '%Y-%m-%d')
end_date_d  = datetime.datetime.strptime(end_date,  '%Y-%m-%d')
while curr_date_d <= end_date_d:

    # current date
    curr_date = str(curr_date_d)[0:10]
    print('--------------------- ' + curr_date +
          ' ---------------------')

    # find file
    yyyy = curr_date[0:4]
    mm   = curr_date[5:7]
    dd   = curr_date[8:10]
    wildcard = file_dir + 'AIRS.' + yyyy + '.' + mm + '.' + dd \
            + '.L3.RetStd_IR001.v6.0.31.1.G*.hdf'
    filename = glob.glob(wildcard)
    if len(filename) != 1:
        print('!!! ERROR !!!')
        exit()
    filename = filename[0]

    # plot
    plot_AIRS3STD_lev(filename, varnames, levels, fig_dir=fig_dir, 
            fig_post=curr_date, scale_dict=scale, 
            cbar_label_dict=cbar_label, title_dict=title,
            vmin_dict=vmin, vmax_dict=vmax)

    # go to next day
    curr_date_d = curr_date_d + datetime.timedelta(days=1)
