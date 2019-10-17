# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: adpusel <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/09/26 12:53:27 by adpusel           #+#    #+#              #
#    Updated: 2019/09/26 12:53:34 by adpusel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = ft_select

LIBFTDIR = libft/
INCSDIR = includes/
SRCSDIR = src/
OBJSDIR = objs/
CC = gcc
CFLAGS = -Wall -Wextra -Werror

HEADER_FILES  = ft_select.defines.h ft_select.h ft_select.prototypes.h ft_select.structures.h
HEADERS =  $(addprefix includes/, $(HEADER_FILES))

# cd render/src; ls -1 | tr '\n' ' ' | pbcopy
SRCS = ft_select.canonical_mode.c ft_select.css.c ft_select.cursor_interaction.c ft_select.cursor_interaction.helpers.c ft_select.get_color_file.c ft_select.getter_0.c ft_select.getter_1.c ft_select.init_termcap.c ft_select.move_display.c ft_select.print.c ft_select.search.c ft_select.search_select.c ft_select.signals.c ft_select.utils_0.c ft_select.utils_1.c main.c 

OBJS = $(addprefix $(OBJSDIR),$(SRCS:.c=.o))


$(OBJSDIR)%.o: $(SRCSDIR)%.c $(HEADERS)
	mkdir -p $(OBJSDIR)
	$(CC) $(CFLAGS) -I $(INCSDIR) -I $(LIBFTDIR)$(INCSDIR) -o $@ -c $<

all: $(NAME)

$(NAME): $(OBJS)
	make -C $(LIBFTDIR)
	$(CC) $(CFLAGS) -o $(NAME) $(OBJS) -L./libft -lft -ltermcap

clean:
	rm -rf $(OBJSDIR)
	make -C $(LIBFTDIR) clean

fclean: clean
	rm -rf $(NAME)
	make -C $(LIBFTDIR) fclean

re: fclean all

.PHONY: all clean fclean re