#sh ./libft/render.sh;

rm -rf render/*
mkdir -p render/includes;
mkdir -p render/src;

cp Makefile render
cp includes/* render/includes
find ./includes -type f -name "*.h" -exec cp {} ./render/includes \; ;
find ./src -type f -name "*.c" -not -name "*test*" -exec cp {} ./render/src \; ;

cp -R ./libft/render render/libft

cd ./render
touch auteur
echo "adpusel" >> auteur
make;

norminette ./src | grep "Error:";
norminette ./includes | grep "Error:";
norminette ./src ./includes