///* ************************************************************************** */
///*                                                                            */
///*                                                        :::      ::::::::   */
///*   ft_atoi.c                                          :+:      :+:    :+:   */
///*                                                    +:+ +:+         +:+     */
///*   By: adpusel <adpusel@student.42.fr>            +#+  +:+       +#+        */
///*                                                +#+#+#+#+#+   +#+           */
///*   Created: 2017/10/19 10:48:07 by adpusel           #+#    #+#             */
///*   Updated: 2017/11/16 12:45:50 by adpusel          ###   ########.fr       */
///*                                                                            */
///* ************************************************************************** */
//
//#include <libft.h>
//
//int expr(t_array *a);
//
//typedef enum
//{
//	INTEGER,
//	PLUS,
//	MINUS,
//	DIV,
//	MUL,
//	P_OPEN,
//	P_CLOSE,
//} e_type;
//
//typedef struct s_token
//{
//	e_type type;
//	int value;
//} t_token;
//
//char *del_space(char *str)
//{
//	while (*str == ' ')
//		str++;
//	return (str);
//}
//
//void lexer(char *str, t_array *array)
//{
//	t_token t;
//	int pos;
//	static char *sign = "+-/*()";
//	static e_type type[10] = { PLUS, MINUS, DIV, MUL, P_OPEN, P_CLOSE };
//
//	while (*str)
//	{
//		ft_bzero(&t, sizeof(t_token));
//		str = del_space(str);
//		if (ft_isdigit(*str))
//		{
//			t.type = INTEGER;
//			t.value = ft_atoi(str);
//			while (ft_isdigit(*str))
//				str += 1;
//		}
//		else if (-1 != (pos = ft_strchr_int(sign, *str)))
//		{
//			t.type = type[pos];
//			t.value = *str;
//			str += 1;
//		}
//		else
//		{
//			printf("error lexer, bad asking");
//			return;
//		}
//		ftarray__push(array, &t);
//	}
//}
//
//int print_token(void *p_el, void *param)
//{
//	t_token *t;
//
//	(void)param;
//	t = p_el;
//	if (t->type == INTEGER)
//		ft_printf("-%d", t->value);
//	else if (t->type == P_OPEN || t->type == P_CLOSE)
//		ft_printf("%c", t->value);
//	else
//		ft_printf(" %c ", t->value);
//	return (0);
//}
//
//// if the token has the right type, I add 1 to the current, and ret true
//int eat(t_array *array, e_type type)
//{
//	t_token *t;
//
//	t = ftarray__current(array);
//	if (t->type == type)
//	{
//		array->i += 1;
//		return (t->value);
//	}
//	ft_printf("error syntax analyze");
//	exit(-42);
//}
//
//int factor(t_array *a)
//{
//	t_token *t;
//	int result;
//
//	t = ftarray__current(a);
//	if (t->type == INTEGER)
//	{
//		return (eat(a, INTEGER));
//	}
//	else
//	{
//		eat(a, P_OPEN);
//		result = expr(a);
//		eat(a, P_CLOSE);
//		return (result);
//	}
//}
//
//int term(t_array *a)
//{
//	t_token *t;
//	int nb;
//	int result;
//
//	result = factor(a);
//	while (NULL != (t = ftarray__current(a))
//		   && (t->type == MUL || t->type == DIV))
//	{
//		if (t->type == MUL)
//		{
//			eat(a, MUL);
//			nb = factor(a);
//			result = result * nb;
//		}
//		if (t->type == DIV)
//		{
//			eat(a, DIV);
//			nb = factor(a);
//			result = result / nb;
//		}
//	}
//	return (result);
//}
//
//int expr(t_array *a)
//{
//	t_token *t;
//	int result;
//
//	result = term(a);
//	while (NULL != (t = ftarray__current(a))
//		   && (t->type == PLUS || t->type == MINUS))
//	{
//		if (t->type == PLUS)
//		{
//			eat(a, PLUS);
//			result = result + term(a);
//		}
//		if (t->type == MINUS)
//		{
//			eat(a, MINUS);
//			result = result - term(a);
//		}
//	}
//	return (result);
//}
//
//// de tout facon a chaque fois j'attends que mon element soit
//// write pour ecrire dedans.
//void fork_and_read()
//{
//
//}
//
//
//int main(int ac, char **av)
//{
//	(void)ac;
//	(void)av;
//
//
//
//	//	t_array *array = ftarray__init(20, sizeof(t_token));
//	//
//	//	lexer(av[1], array);
//	//	ftarray__func(array, print_token, NULL);
//	//	ft_printf("\n");
//	//	array->i = 0;
//	//	ft_printf("%d\n", expr(array));
//	//	return (0);
//}





#include <zconf.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <libft.h>

void write_in_file(char *text)
{
	int file_fd = open("toto.txt", O_CREAT | O_WRONLY | O_APPEND, 0644);

	write(file_fd, text, ft_strlen(text));
	close(file_fd);
}


int main(void)
{
	int status;
	int i;

	// arguments for commands; your parser would be responsible for
	// setting up arrays like these

	// j'ai un fd pour mon programme, j'ai juste a l'ajouter pour faire les pipes ! yeah !
	char *cat_args[] = { "cat", "scores", NULL };
	char *grep_args[] = { "grep", "Villanova", NULL };
	char *cut_args[] = { "cut", "-b", "1-10", NULL };

	// make 2 pipes (cat to grep and grep to cut); each has 2 fds

	int pipes[4];
	pipe(pipes); // sets up 1st pipe
	pipe(pipes + 2); // sets up 2nd pipe

	// we now have 4 fds:
	// pipes[0] = read end of cat->grep pipe (read by grep)
	// pipes[1] = write end of cat->grep pipe (written by cat)
	// pipes[2] = read end of grep->cut pipe (read by cut)
	// pipes[3] = write end of grep->cut pipe (written by grep)

	// Note that the code in each if is basically identical, so you
	// could set up a loop to handle it.  The differences are in the
	// indicies into pipes used for the dup2 system call
	// and that the 1st and last only deal with the end of one pipe.

	// fork the first child (to execute cat)

	if (fork() == 0)
	{
		// replace cat's stdout with write part of 1st pipe

		dup2(pipes[1], 1);

		// close all pipes (very important!); end we're using was safely copied

		close(pipes[0]);
		close(pipes[1]);
		close(pipes[2]);
		close(pipes[3]);

		execvp(*cat_args, cat_args);
	}
	else
	{
		// fork second child (to execute grep)

		if (fork() == 0)
		{
			// replace grep's stdin with read end of 1st pipe


			dup2(pipes[0], 0);

			// replace grep's stdout with write end of 2nd pipe

			dup2(pipes[3], 1);

			// close all ends of pipes

			close(pipes[0]);
			close(pipes[1]);
			close(pipes[2]);
			close(pipes[3]);

			execvp(*grep_args, grep_args);
			printf("truc");
			write_in_file("toto");
		}
		else
		{
			// fork third child (to execute cut)

			if (fork() == 0)
			{
				// replace cut's stdin with input read of 2nd pipe

				dup2(pipes[2], 0);

				// close all ends of pipes

				close(pipes[0]);
				close(pipes[1]);
				close(pipes[2]);
				close(pipes[3]);
				write_in_file("tata");
				execvp(*cut_args, cut_args);
			}
		}
	}

	// only the parent gets here and waits for 3 children to finish

	close(pipes[0]);
	close(pipes[1]);
	close(pipes[2]);
	close(pipes[3]);

	for (i = 0; i < 3; i++)
		wait(&status);
	write_in_file("titi");
}