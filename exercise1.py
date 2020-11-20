import numpy as np
import matplotlib.pyplot as plt

class exercise():
    def __init__(self, scale=1, sigma=1, pad=0.5):
        self.scale = scale
        data = np.genfromtxt('trajectories_for_test.txt', delimiter=' ').astype(float)
        self.sigma = sigma
        self.pad = pad
        self.xmin, self.ymin = np.min(data[:, 2:4], axis=0)
        # Shift the x and y coordinates from zero centralized to positive
        self.data = np.subtract(data, [0, 0, self.xmin, self.ymin])
        # Scale the x and y coordinates from meter to decimeter (default unit meters and scale=10)
        self.data = np.multiply(self.data, [1, 1, self.scale, self.scale])
        # Compute the height and width of the maps
        self.dimensions = np.flip(np.ceil(np.max(self.data[:, 2:4], axis=0)).astype(int))
        # Very important, the order of userId should be obtained


        ped_ids = []
        for ped_id in self.data[:,1]:
            if ped_id not in ped_ids:
                ped_ids.append(ped_id)
        self.ped_ids = np.asarray(ped_ids)

        fig,ax = plt.subplots()
        ax.set_aspect('equal')
        offsets = np.empty((0, 6))
        sorted_data = np.empty((0, 4))
        for ped_id in self.ped_ids:
            ped_traj = self.data[self.data[:, 1] == ped_id, :]
            #print("{} pedestrin:\n".format(ped_id),ped_traj)
            # the initialized sorted data is empy. With that we
            # can put the data for every pedestrain stacked
            sorted_data = np.vstack((sorted_data, ped_traj))
            #print(sorted_data)
            #print(ped_traj[1:, 2:4])
            # through slices we can get the offset
            ped_offset = ped_traj[1:, 2:4] - ped_traj[:-1, 2:4]
            ped_offset = np.concatenate((ped_traj[1:, :], ped_offset), axis=1)
            print(ped_offset)
            offsets = np.vstack((offsets, ped_offset))
            ax.plot(ped_traj[:, 2], ped_traj[:, 3])
        theta = np.arctan2(offsets[:, 5], offsets[:, 4])
        velocity = np.linalg.norm(offsets[:, 4:6], axis=1) / 0.4

        offsets = np.concatenate((offsets, theta.reshape(-1, 1), velocity.reshape(-1, 1)), axis=1)
        ax.set_title("Trajectories")
        plt.gca().invert_yaxis()
        plt.show()
        plt.gcf().clear()
        plt.close()

        self.offsets = offsets
        self.min_speed = np.min(self.offsets[:, -1])
        self.max_speed = np.max(self.offsets[:, -1])

        sorted_data = np.divide(sorted_data, [1, 1, self.scale, self.scale])
        self.sorted_data = np.add(sorted_data, [0, 0, self.xmin, self.ymin])

    def motion_map(self, offsets=None, max_speed=50):
        """
        This is the function to convert the motion in into a motion map
        Return speed map and orientation map
        """
        speed_map = np.zeros((self.dimensions))
        orient_map = np.zeros((self.dimensions))
        count = np.zeros((self.dimensions))
        if np.all(offsets) == None:
            offsets = self.offsets

        if max_speed:
            # clip the very unlikely speed
            offsets[:, -1] = np.clip(offsets[:, -1], a_min=0, a_max=max_speed)

        for offset in offsets:
            x, y, delta_x, delta_y = offset[2:6]
            print("x:",x)
            print("y:",y)
            print("delta_x:", delta_x)
            print("delta_y:", delta_y)
            print(sorted((x, x + delta_x)))
            xl, xr = sorted((x, x + delta_x))
            xl, xr = max(0, int(xl - self.pad)), min(int(xr + self.pad), self.dimensions[1])
            yl, yr = sorted((y, y + delta_y))
            yl, yr = max(0, int(yl - self.pad)), min(int(yr + self.pad), self.dimensions[0])
            # count the frequency for normalization
            count[yl:yr, xl:xr] += 1
            speed_map[yl:yr, xl:xr] += offset[-1]
            orient_map[yl:yr, xl:xr] += (offset[-2] + np.pi) / (2 * np.pi)

        def normalize(count, data):
            norm_data = np.zeros_like(data)
            for i, row in enumerate(data):
                for j, value in enumerate(row):
                    if count[i, j] != 0:
                        norm_data[i, j] = value / count[i, j]
            return norm_data

        orient_map = normalize(count, orient_map)
        speed_map = normalize(count, speed_map)
        # speed_map = speed_map/self.max_speed
        speed_map = speed_map / max_speed

        assert np.max(orient_map) <= 1 and np.max(orient_map) >= 0, print("orient_map contains invalid values",
                                                                          np.max(orient_map), np.min(orient_map))
        assert np.max(speed_map) <= 1 and np.max(speed_map) >= 0, print("speed_map contains invalid values",
                                                                        np.max(speed_map), np.min(speed_map))
        return orient_map, speed_map



e = exercise()
e.motion_map(e.offsets,e.max_speed)
