class Ninja:
    def __init__(self, num_tree: int, max_distance):
        # set initial var
        self.num_tree = num_tree
        self.max_distance = max_distance
        self.intial_trees_list = []

        # run init setting
        self.get_initial_setting()

    def get_initial_setting(self):
        # get input of trees' height
        tree_height_list = [int(input("Input height")) for _ in range(self.num_tree)]
        # make list of trees info dict
        count = 0
        for _ in range(self.num_tree):
            self.intial_trees_list = self.create_tree_dict(tree_height_list)
            count += 1

    def calc_total_distance(self, trees_info_list: list):
        total_distance = 0
        for tree_dict in trees_info_list:
            current_height_rank = tree_dict["height_rank"]

            # find next ranked tree and calc distance
            for next_rank_tree_dict in trees_info_list:
                if next_rank_tree_dict["height_rank"] == current_height_rank + 1:

                    # add to total_distance
                    distance = abs(next_rank_tree_dict["position"] - tree_dict["position"])
                    if distance > self.max_distance:
                        return 0
                    total_distance += distance
        return total_distance

    @staticmethod
    def position_mover(trees_into_list: list, ps_rank_to_move: int, step: int) -> list:
        for target_ps_rank in range(ps_rank_to_move, trees_into_list[-1]["position_rank"] + 1):
            trees_into_list[target_ps_rank]["position"] += step
        return trees_into_list

    def get_max_distance_tree_list(self):

        max_distance = 0
        for step in range(self.max_distance):
            for ps_rank in range(self.num_tree):
                moved_tree_list = self.position_mover(self.intial_trees_list, ps_rank, step)
                current_distance = self.calc_total_distance(moved_tree_list)
                if current_distance > max_distance:
                    max_distance = current_distance

        return max_distance

    @staticmethod
    def create_tree_dict(height_list: list):
        tree_info_list = []

        # make height ranked list
        seq = sorted(height_list)
        height_ranked_list = [seq.index(v) for v in height_list]

        position_rank_count = 0
        for height, height_rank in zip(height_list, height_ranked_list):
            tree_info_list.append({
                "hegith": height,
                "height_rank": height_rank,
                "position": position_rank_count,
                "position_rank": position_rank_count,
            })
            position_rank_count += 1
        return tree_info_list


a = Ninja(num_tree=4, max_distance=3)
max_distance = a.get_max_distance_tree_list()
print(max_distance)
