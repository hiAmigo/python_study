class Student():

    @property
    def score(self):
        print('score get方法？？')
        return self._score

    @score.setter
    def score(self, score):
        print('score set方法!!!')
        if not isinstance(score, int):
            raise ValueError('成绩的类型不对')
        if score < 0 or score > 100:
            raise ValueError('成绩不合法')
        self._score = score

    # @score.getter
    # def score(self):
    #     return self._score

s = Student()
s.score = 76
print(s.score)


    