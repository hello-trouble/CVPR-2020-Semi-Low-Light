import os
from data import srdata
import glob

class LowLightTest(srdata.SRData):
    def __init__(self, args, name='LowLightTest', train=True, benchmark=False):
        super(LowLightTest, self).__init__(
            args, name=name, train=train, benchmark=benchmark
        )

    def _set_filesystem(self, dir_data):
        super(LowLightTest, self)._set_filesystem(dir_data)
        self.apath = '/data1/yangwenhan/datasets/'
        print(self.apath)
        self.dir_hr = os.path.join(self.apath, 'Our_normal_test')
        self.dir_lr = os.path.join(self.apath, 'Our_low_test')

    def _scan(self):
        names_hr, names_lr = super(LowLightTest, self)._scan()
        names_hr = names_hr[self.begin - 1:self.end]
        names_lr = names_lr[self.begin - 1:self.end]

        return names_hr, names_lr
