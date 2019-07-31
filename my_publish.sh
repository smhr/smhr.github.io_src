#rsync -avh ./output/ ../../smhr.github.io_output_git/
rsync -avh ./public/ ../../smhr.github.io_output_git/
git push origin master
git push gitlab master
