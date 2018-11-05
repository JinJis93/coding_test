import random

test_n = 30


class Prob13412:
    max_test_case_num = 10000

    def __init__(self, t: int):
        self.t = t
        self.case_test_list = [random.randrange(self.max_test_case_num + 1) for _ in range(self.t)]

    def run(self):
        # print inputs
        print("here are inputs")
        print(self.t)
        for input_num in self.case_test_list:
            print(input_num)

        # print output
        print("here are outputs")
        for output_num in self.get_combination_count_list():
            print(output_num)

    def get_combination_count_list(self) -> list:
        comb_count_list = []
        # iterate case_test_list
        for target_num in self.case_test_list:
            # 1부터 target_num 까지 리스트 생성
            count = 0
            for num_a in range(1, target_num + 1):
                # sort out those num that does not devide target_num exactly
                if not target_num % num_a == 0:
                    continue
                num_b = int(target_num / num_a)
                if self.calc_gcd(num_a, num_b) == 1 and self.calc_lcm(num_a, num_b) == (num_a * num_b):
                    count += 1
            # because it is combination, divide by 2 to exclude repeated nums
            comb_count_list.append(int(count / 2))

        return comb_count_list

    @staticmethod
    def calc_gcd(a: int, b: int):
        # 초기 최대공약수 설정
        current_gcd = 1
        for cd in range(1, min(a, b) + 1):
            # 공약수가 a, b에 모두 나눠떨어질시
            if a % cd == 0 and b % cd == 0:
                if cd > current_gcd:
                    current_gcd = cd
        return current_gcd

    @staticmethod
    def calc_lcm(a: int, b: int):
        # 최소공약수 구하기
        gcm = Prob13412.calc_gcd(a, b)
        return gcm * (a // gcm) * (b // gcm)


test1 = Prob13412(10)
test1.run()
