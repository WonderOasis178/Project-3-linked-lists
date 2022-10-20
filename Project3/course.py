''' Course Class for Project 3 of cs2420 '''


class Course:
    ''' Course object '''

    def __init__(self, number=0, name="", credit_hr=0.0, grade=0.0):
        # validation
        if not isinstance(number, int):
            raise ValueError("Number must be an integer")
        elif not isinstance(name, str):
            raise ValueError("Name must be a string")
        elif not isinstance(credit_hr, float):
            raise ValueError("Credit hrs must be of type float")
        elif not isinstance(grade, float):
            raise ValueError("Grade must be of type float")
        while not (grade <= 4.0 and grade >= 0.0):
            raise ValueError("Grade not valid")
        self._number = number
        self._name = name
        self._credit_hr = credit_hr
        self._grade = grade

        self.next = None
        self.previous = None

        self.results = self.__str__()

    def number(self):
        """this function takes no parameter and returns
           number of this course object"""
        try:
            if self._number is float:
                raise ValueError
            self._number = int(self._number)
        except (TypeError, ValueError, IndexError) as some_num_error:
            raise some_num_error
        return self._number

    def name(self):
        """this is a getter method to return name attribute
            of course object"""
        try:
            self._name = str(self._name)
        except (TypeError, ValueError, IndexError) as some_name_error:
            raise some_name_error
        return self._name

    def credit_hr(self):
        """this is a getter method to return credit attribute
            of course object"""
        try:
            self._credit_hr = float(self._credit_hr)
        except (TypeError, ValueError, IndexError) as some_credit_error:
            raise some_credit_error
        return self._credit_hr

    def grade(self):
        """this is a getter method to return grade attribute
            of course object"""
        try:
            if float(self._grade) <= 4.0 and float(self._grade) >= 0.0:
                self._grade = float(self._grade)
            else:
                raise ValueError
        except (TypeError, ValueError, IndexError) as some_grade_error:
            raise some_grade_error
        return self._grade

    def __str__(self):
        """returns the string representation of this object"""
        self.done = 'cs' + str(self.number()) + ' ' + self.name() + ' Grade:' + \
            str(self.grade()) + ' ' + 'Credit Hours:' + str(self.credit_hr())
        return self.done

    def __eq__(self, other):
        '''Equals'''
        cnum = other
        if isinstance(other, Course):
            cnum = other._number()
        return self._number() == cnum

    def __ne__(self, other):
        '''Not'''
        cnum = other
        if isinstance(other, Course):
            cnum = other._number()
        return self._number() != cnum

    def __lt__(self, other):
        '''Less than'''
        cnum = other
        if isinstance(other, Course):
            cnum = other._number()
        return self._number() < cnum

    def __gt__(self, other):
        '''Greater than'''
        cnum = other
        if isinstance(other, Course):
            cnum = other._number()
        return self._number() > cnum

    def __le__(self, other):
        '''Less or equals'''
        cnum = other
        if isinstance(other, Course):
            cnum = other._number()
        return self._number() <= cnum

    def __ge__(self, other):
        '''Greater or equals'''
        cnum = other
        if isinstance(other, Course):
            cnum = other._number()
        return self._number() >= cnum
