def one_argument(one):
    pass


def two_arguments(one, two):
    pass


def multiple_arguments(one, two, three):
    pass


class Foo:
    def bar(self, one, two, three):
        pass


one_argument(1)
one_argument(one=1)
two_arguments(1, 2)
two_arguments(one=1, two=2)
multiple_arguments(one=1, two=2, three=3)
multiple_arguments(1, 2, 3)

Foo.bar(1, 2, 3)
Foo.bar(one=1, two=2, three=3)
