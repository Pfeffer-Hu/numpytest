"""
也就是说clip这个函数将将数组中的元素限制在a_min, a_max之间，大于a_max的就使得它等于 a_max，小于a_min,的就使得它等于a_min


"""

import numpy as np
x=np.array([1,2,3,5,6,7,8,9])
np.clip(x,3,8)
