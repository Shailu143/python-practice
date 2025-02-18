# python-practice
Practice Python Coding

Git Commands to checkout only specific project folder.

To checkout only a specific folder within repository
1. git clone --no-checkout git@github.com:Shailu143/python-practice.git

   cd python-practice 

3. If you want to checkout parent folder’s files

   git sparse-checkout init --cone
   
5. If you don’t want parent folder’s files

   git sparse-checkout init --no-cone

7. git sparse-checkout set py-oop-proj1

8. git checkout

9. If you want full repository again
   
	git sparse-checkout disable

	git checkout .

10. To push only specific folder
    
	git add py-oop-proj1

	git commit -m "Updated py-oop-proj1"

	git push origin main
