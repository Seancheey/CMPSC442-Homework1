############################################################
# CMPSC 442: Homework 1
############################################################

student_name = "Qiyi Shan"

############################################################
# Section 1: Python Concepts
############################################################

python_concepts_question_1 = """
Strongly typed means that every type conversion need specific opeartion.
    For example, a string cannot be converted to int when doing "abc" + 3
Dynamically typed means that the type of variables are detrermined during runtime, rather than compile time.
    For example, we can do following function define easily:
     def add(a,b):
         return a+b
    So that when we do add("a","b") it returns "ab" and when we do add(1,2) it returns 3
"""

python_concepts_question_2 = """
The python dictionary is implemented by hashtable, and therefore, in order for something to be a dictionary key in python, it must be hashable, i.e. has __hash__() function implemented.
The reason that python list does not support __hash__() function is that list is a container that it makes no sense to compare list without specific pointed out how to compare. So it is possible that two lists with same values but different pointers will give different hash values and cause serious problems because of that.
"""

python_concepts_question_3 = """
Because string in Python is immutable, join() is a faster implementaton, as join would not allocate new memory in each iteration while using for and result += s would cause python to allocate new memory and slow the execution.
"""

############################################################
# Section 2: Working with Lists
############################################################

def extract_and_apply(l, p, f):
    return [f(ele) for ele in l if p(ele)]

def concatenate(seqs):
    return [ele for seq in seqs for ele in seq]

def transpose(matrix):
    col_len = len(matrix[0])
    row_len = len(matrix)
    return [[matrix[y][x] for y in xrange(row_len)] for x in xrange(col_len)]

############################################################
# Section 3: Sequence Slicing
############################################################

def copy(seq):
    return seq[:]

def all_but_last(seq):
    return seq[:-1]

def every_other(seq):
    return seq[::2]

############################################################
# Section 4: Combinatorial Algorithms
############################################################

def prefixes(seq):
    for i in xrange(len(seq)+1):
        yield seq[:i]


def suffixes(seq):
    for i in xrange(len(seq)+1):
        yield seq[i:]

def slices(seq):
    for i in xrange(len(seq)):
        for j in xrange(i,len(seq)):
            if len(seq[i:j+1]) != 0:
                yield seq[i:j+1]


############################################################
# Section 5: Text Processing
############################################################

def normalize(text):
    return " ".join(text.lower().split())

def no_vowels(text):
    return "".join([c for c in text if c not in "aeiouAEIOU"])

def digits_to_words(text):
    word_map = {
    0:"zero", 1:"one", 2:"two", 3:"three", 4:"four", 5:"five",
    6:"six", 7:"seven", 8:"eight", 9:"nine"
    }
    return " ".join([word_map[int(c)] for c in text if c in "0123456789"])

def to_mixed_case(name):
    parts = [p for p in name.split("_") if p != ""]
    return "".join([parts[0].lower()]+[p[0].upper()+p[1:].lower() for p in parts[1:]])


############################################################
# Section 6: Polynomials
############################################################

class Polynomial(object):

    def __init__(self, polynomial):
        self.poly = polynomial

    def get_polynomial(self):
        return tuple(self.poly)

    def __neg__(self):
        return Polynomial([(-item[0],item[1]) for item in self.poly])

    def __add__(self, other):
        return Polynomial(list(self.get_polynomial())+list(other.get_polynomial()))

    def __sub__(self, other):
        return (self + (- other))

    def __mul__(self, other):
        return Polynomial([(coef1*coef2,ind1+ind2) for coef1,ind1 in self.get_polynomial() for coef2,ind2 in other.get_polynomial()])

    def __call__(self, x):
        return sum([coef * x**index for coef,index in self.poly])

    def simplify(self):
        coefs = {}
        for coef,ind in self.poly:
            if ind not in coefs:
                coefs[ind] = coef
            else:
                coefs[ind] += coef
        self.poly = [(coef,ind) for ind, coef in coefs.items() if coef!=0]
        self.poly.sort(key=lambda x:x[1],reverse=True)
        if self.poly == []:
            self.poly = [(0,0)]

    def __str__(self):
        out = [
        (" + " if coef>=0 else " - ",
        "" if abs(coef)==1 and ind!=0 else str(abs(coef)),
        "" if ind==0 else "x" if ind==1 else "x^%d"%ind)
        for coef,ind in self.get_polynomial()
        ]
        out1 = [("-" if out[0][0]==" - " else "")+out[0][1]+out[0][2]]+[a+b+c for a,b,c in out[1:]]
        return "".join(out1)

    def _max_index(self):
        return max(self.poly,key=lambda x:x[1])[1]

    def _get_coef(self,index):
        for i in range(len(self.get_polynomial())):
            if self.get_polynomial()[i][1] == index:
                return self.get_polynomial()[i][0]
        return 0

############################################################
# Section 7: Feedback
############################################################

feedback_question_1 = """
I spent about 4 hours on this assignment.
"""

feedback_question_2 = """
The last part of the assignemnt spent most of my time. I should not say that it is hard, but I misinterpreted some problems (that at first place I always simplified answer after mul/add/sub).
Overall, debugging and trying to get every questions correct spent my even more than the assignment it self.
"""

feedback_question_3 = """
Ovreall I like this assignment as a whole which helped me reviewed a lot of concepts. At first place I didn't know what is strong-typed and how to concatenate seqs with double 'for' in a list comprehension.
"""
def unit_test():
    unit_test12345()
    unit_test6()

def unit_test12345():
    print "===testing part2"
    assert(extract_and_apply([1,2,3,4,5],lambda x:x<4,lambda x:x**2)==[1,4,9])
    assert(concatenate([[1, 2], [3, 4]])==[1,2,3,4])
    assert(transpose([[1, 2, 3]])==[[1], [2], [3]])
    assert(transpose([[1, 2], [3, 4], [5, 6]])==[[1, 3, 5], [2, 4, 6]])
    print "===testing part3"
    a = "abc"
    b = copy(a)
    a+="asdf"
    assert(b=="abc")
    assert(all_but_last("abc")=="ab")
    assert(all_but_last((1,2,3)) == (1,2))
    assert(every_other([1,2,3,4,5])==[1,3,5])
    assert(every_other("abcdef")=="ace")
    print "===testing part4"
    assert(list(prefixes([1, 2, 3]))==[[], [1], [1, 2], [1, 2, 3]])
    assert(list(suffixes([1, 2, 3]))==[[1, 2, 3], [2, 3], [3], []])
    assert(list(slices([1,2,3]))==[[1], [1, 2], [1, 2, 3], [2], [2, 3], [3]])
    assert(list(slices("abc"))==['a', 'ab', 'abc', 'b', 'bc', 'c'])
    print "===testing part5"
    assert(normalize("This   is An eXamPle.     ")=='this is an example.')
    assert(no_vowels("We love Python Aye!") == "W lv Pythn y!")
    assert(digits_to_words("Zip Code: 19104")=="one nine one zero four")
    assert(digits_to_words("Pi is 3.1415...")=='three one four one five')
    assert(digits_to_words("2asd687")=="two six eight seven")
    assert(to_mixed_case('to_mixed_case')=='toMixedCase')
    assert(to_mixed_case('__EXAMPLE__NAME__TEST__')=='exampleNameTest')

def unit_test6():
    print "===testing part6"
    p, q = Polynomial([(2,1),(1,0)]), Polynomial([(2,1),(-1,0)])
    p0,p1 = Polynomial([(0,1),(2,3)]),Polynomial([(1, 2), (5, 0), (3, 1)])
    # get_polynomial test
    assert(type(p1.get_polynomial())==tuple)
    print "p:",p.get_polynomial()
    assert(p.get_polynomial() == ((2,1),(1,0)))
    print "p1:",p1.get_polynomial()
    assert(p1.get_polynomial() == ((1, 2), (5, 0), (3, 1)))
    # neg test
    assert(type(-p1) == Polynomial)
    print "-p:",(-p).get_polynomial()
    assert((-p).get_polynomial() == ((-2,1),(-1,0)))
    print "-p1:",(-p1).get_polynomial()
    assert((-p1).get_polynomial() == ((-1, 2), (-5, 0), (-3, 1)))
    # add test
    assert(type(p+p) == Polynomial)
    print "p+p:",(p+p).get_polynomial()
    assert((p+p).get_polynomial() == ((2, 1), (1, 0), (2, 1), (1, 0)))
    print "p+q:",(p+q).get_polynomial()
    assert((p+q).get_polynomial() == ((2, 1), (1, 0), (2, 1), (-1, 0)))
    # sub test
    assert(type(p-p) == Polynomial)
    print "p-p:",(p-p).get_polynomial()
    assert((p-p).get_polynomial() == ((2, 1), (1, 0), (-2, 1), (-1, 0)))
    # mul test
    assert(type(p1*p1) == Polynomial)
    print "p*p:",(p*p).get_polynomial()
    assert((p*p).get_polynomial() == ((4, 2), (2, 1), (2, 1), (1, 0)))
    print "p1*p1:",(p1*p1).get_polynomial()
    assert((p1*p1).get_polynomial() == ((1, 4), (5, 2), (3, 3), (5, 2), (25, 0), (15, 1), (3, 3), (15, 1), (9, 2)))
    # call test
    print [p1(x) for x in range(5)]
    assert(tuple([p1(x) for x in range(5)])==(5, 9, 15, 23, 33))
    # simplify test
    res2 = p0 * p0
    assert(res2.simplify() is None)
    print "p0 * p0:",res2.get_polynomial()
    assert(res2.get_polynomial()==((4, 6),))
    # string test
    p = Polynomial([(1,1),(1,0)])
    ans_map = {
        p : "x + 1",
        p+p: "2x + 2",
        -p: "-x - 1",
        -p-p: "-2x - 2",
        p*p: "x^2 + 2x + 1",
        Polynomial([(3,3),(-1,1)]): "3x^3 - x"
    }
    for p,ans in ans_map.items():
        p.simplify()
        print "__str__:", str(p), "versus answer:", ans
        assert(str(p)==ans)

    ans_map_no_simp = {
        p0:"0x + 2x^3",
        p0*p0:"0x^2 + 0x^4 + 0x^4 + 4x^6",
        -p0*p0:"0x^2 + 0x^4 + 0x^4 - 4x^6"
    }
    for p,ans in ans_map_no_simp.items():
        print "__str__:", str(p), "versus answer:", ans
        assert(str(p)==ans)

if __name__ == "__main__":
    unit_test()
