#[6] Find student from CS department where the roll number may be in capital or smallcase letters

rno=input("enter your roll number:")
if 'cs' in rno or 'CS' in rno or 'Cs' in rno or 'cS' in rno:
    print("Student of Computer science")
else:
    print("Other department")