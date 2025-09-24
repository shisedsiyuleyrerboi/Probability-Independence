import random
import os

# SEED SELECTION #
os.system('clear')
student_code = int(input('# Student Code: '))

if(student_code % 2 == 0):
    random.seed(45)
else:
    random.seed(46)

n = int(input('# of Simulations: '))
os.system('clear')

# FIRST SCENARIO LOGIC #
sample_space = [1, 2, 3, 4, 5, 6] 
prob_w_sc1 = 1/6
error_bias = pow(10, -6)

even_numbers_sample_space = []
odd_numbers_sample_space = []
sum_even_numbers_probability = 0
sum_odd_numbers_probability = 0

for s in sample_space:
    if (s % 2 == 0):
        even_numbers_sample_space.append(s)
        sum_even_numbers_probability += prob_w_sc1
    else:
        odd_numbers_sample_space.append(s)
        sum_odd_numbers_probability += prob_w_sc1

event_a = set(odd_numbers_sample_space)
event_b = set(even_numbers_sample_space)
event_c = set([1, 6])
event_a_or_c = list(event_a.union(event_c))
event_1_or_6 = list(event_c)

prob_event_a = sum_odd_numbers_probability
prob_event_b = sum_even_numbers_probability
prob_event_c = len(event_c) * prob_w_sc1
prob_event_axb = prob_event_a * prob_event_b
prob_event_a_or_c = len(event_a_or_c) * prob_w_sc1

intersection_a_and_b = list(event_a.intersection(event_b))
intersection_a_and_c = list(event_a.intersection(event_c))
prob_intersection_a_and_c = len(intersection_a_and_c) * prob_w_sc1
x_minus_y_1 = 0 - prob_event_axb
x_minus_y_2 = prob_intersection_a_and_c - (prob_event_a * prob_event_c)

#EXPERIMENT LOGIC WITH N TRIES#
results = []
for r in range(0, n):
    prob_w = int(random.choice(sample_space))
    results.append(prob_w)

even_numbers_exp = []
odd_numbers_exp = []
for r in results:
    if(r % 2 == 0):
        even_numbers_exp.append(r)
    else:
        odd_numbers_exp.append(r)

print('-----------First Scenario-----------------------------')
print(f'Given the Sample Space      = {sample_space}')
print(f'Probability of each element : {prob_w_sc1*100:.2f}%')
print(f'Event A (All odd numbers)   : {odd_numbers_sample_space[0:6]}           P(A) = {prob_event_a:.2f}')
print(f'Event B (All even numbers)  : {even_numbers_sample_space[0:6]}           P(B) = {prob_event_b:.2f}')
print(f'Event C (1 or 6)            : {event_1_or_6}              P(C) = {prob_event_c:.2f}')
print(f'Event A or C                : {event_a_or_c}        P(A or C) = {prob_event_a_or_c:.2f}\n'), 

print('-----------Experiment Results------------------------')
print(f'Given {n} tries')
print(f'Given the Sample Space      = {sample_space}')
print(f'Probability of each element : {prob_w_sc1*100:.2f}%')
print(f'Event A (All even numbers)  : {even_numbers_exp}')
print(f'Event B (All odd numbers)   : {odd_numbers_exp}\n')

print('------------Event Independence--------------------')
print(f'Since A and B = {intersection_a_and_b}, P(A and B) = 0, P(A) x P(B) = {prob_event_axb:.2f}')
if (abs(x_minus_y_1) >= error_bias):
    print('First result: A and B are not independent.\n')
else:
    print('First result: A and B are independent.\n')
print(f'Since A and C = {intersection_a_and_c}, P(A and C) = {prob_intersection_a_and_c:.2f}, P(A) x P(C) = {(prob_event_a * prob_event_c):.2f}')
if (abs(x_minus_y_2) >= error_bias):
    print('Second result: A and C are not independent.\n')
else:
    print('Second result: A and C are independent.\n')

