"""
Created on September 9, 2019

@author: Yi Wang
"""

import datetime
import glob

from mylib.plot_airs import plot_AIRS3STD_col

#######################
# Start user parameters
#

# Starting date
start_date = '2017-08-01'

# Ending date
end_date = '2017-09-30'

varnames = ['TotCO_A', 'TotCO_D']

vmin = {
        'TotCO_A': 0.0,
        'TotCO_D': 0.0,
        }
vmax = {
        'TotCO_A': 4.0e18,
        'TotCO_D': 4.0e18,
        }

scale = {
        }

cbar_label = {
        'TotCO_A': r'CO [molecules cm$^{-2}$]',
        'TotCO_D': r'CO [molecules cm$^{-2}$]',
        }

title = {
        'TotCO_A': 'CO vertical column density (ascending orbit)',
        'TotCO_D': 'CO vertical column density (descending orbit)',
        }

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
    plot_AIRS3STD_col(filename, varnames, fig_dir=fig_dir, 
            fig_post=curr_date, scale_dict=scale, 
            cbar_label_dict=cbar_label, title_dict=title,
            vmin_dict=vmin, vmax_dict=vmax)

    # go to next day
    curr_date_d = curr_date_d + datetime.timedelta(days=1)
