min = 60;
second = 60;

print(min * second * 2);

# types of data

x = 20;
y = "20";

sum1 = x + x;
# sum2 = x + y;
sum3 = y + y;

print(sum1, sum3);
print(type(sum1), type(sum3));
print(type(y));
z= int(y);
print(type(z));

# Lists

student_marks = [ 88, 76, 93, 85];
print(type(student_marks));
# List with Range
student_marksRange = list(range(50, 63));
print(student_marksRange);
# with step : mane koto por por
student_marksRange2 = list(range(50, 63, 3)); 
print(student_marksRange2);

# use dir() in python shell....see all things and help to find what it does
heloo = "hello world"
print(heloo.upper());
