# sarit malayev 311397582
# question 3
def compare_subjects_within_student(subj1_all_students,
                                    subj2_all_students):
    """
    Compare the two subjects with their students and print out the "preferred"
    subject for each student. Single-subject students shouldn't be printed.

    Choice for the data structure of the function's arguments is up to you.
    """
    a=len(subj1_all_students)
    b=len(subj2_all_students)
    
    l={}
    max_sub2={}
    max_sub1={}

    for i in subj1_all_students:
         max_sub1[i]=max(subj1_all_students[i])
    for i in subj2_all_students:
         max_sub2[i]=max(subj2_all_students[i])
    print(max_sub1)
    print(max_sub2)
    if a>b:
        for k in max_sub2:
            for j in max_sub1:
                if k==j:
                    if max_sub2[k]>max_sub1[j]:
                        l[k]= 'subj2_all_students'
                    else:
                        l[k]= 'subj1_all_students'
    else:
        for k in max_sub1:
            for j in max_sub2:
                if k==j:
                    if max_sub1[k]>max_sub2[j]:
                        l[k]= 'subj1_all_students'
                    else:
                        l[k]= 'subj2_all_students'


                    
    return l


math= {'Arik': [95,80], 'Noa': [70,65], 'Uriel': [80, 70], 'Lea': [85,80], 'Sigal': [80,90]}
history= {'Arik': [85,80], 'Noa': [75,80], 'Uriel': [75, 65], 'Lea': [95,80]}
result=compare_subjects_within_student(math,history)
for i in result:
    if result[i]=='subj1_all_students':
        result[i]='math'
    else:
        result[i]='history'
print(result)
