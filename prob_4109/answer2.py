from itertools import combinations


class NinjaGame:

    def __init__(self, max_jump_distance: int, tree_list: list):
        self.max_jump_distance = max_jump_distance
        self.tree_list = tree_list
        self.ranked_tree_list = None

    def get_all_position_comb(self):
        return combinations(range((len(self.tree_list) - 1) * self.max_jump_distance), len(self.tree_list))

    def get_max_distance_and_its_info_dict(self):
        # make ranked_list
        ascending_order = sorted(self.tree_list)
        ranked_list = [ascending_order.index(height) for height in self.tree_list]

        max_distance = None
        max_comb = None
        for position_comb in self.get_all_position_comb():

            current_distance = 0
            for index in range(len(self.tree_list)):
                # if reached last index, quit
                if index == len(self.tree_list) - 1:
                    break
                distance = abs(position_comb[ranked_list.index(index)] - position_comb[ranked_list.index(index + 1)])
                if distance > self.max_jump_distance:
                    break
                # else
                current_distance += distance

            # if no max_distance configured, set initial one
            if max_distance is None and max_comb is None:
                max_distance = current_distance
                max_comb = position_comb
                continue

            # finally, compare current distance with max_distance
            if current_distance > max_distance:
                max_distance = current_distance
                max_comb = position_comb

        return abs(max_comb[ranked_list.index(0)] - max_comb[ranked_list.index(len(self.tree_list) - 1)])


test_ninja_instance = NinjaGame(max_jump_distance=4, tree_list=[10, 30, 20, 40])
print(test_ninja_instance.get_max_distance_and_its_info_dict())
