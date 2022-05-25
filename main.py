import random


def main():
    while True:
        print("\t\t_________________________________________")
        print("\t\t\t -------Main Menu-------")
        print("\t\t_________________________________________")
        print("\t\t\t1-> Administrator")
        print("\t\t\t2-> Client")
        print("\t\t\t3-> Exit")
        choice1 = eval(input("\t\t\tEnter your choice(1/2/3):-"))
        if choice1 == 1:
            admin()
        elif choice1 == 2:
            client()
        elif choice1 == 3:
            exit()
        else:
            print("Invalid input")


def admin():
    while True:
        Password = input("Enter Your Password:-")
        if Password == "admin":
            while True:
                print("\t\t_________________________________________")
                print("\t\t\t -------Admin Menu-------")
                print("\t\t_________________________________________")
                print("\t\t\t1-> Add Movies")
                print("\t\t\t2-> Remove Movies")
                print("\t\t\t3-> Edit Movie Timings")
                print("\t\t\t4-> Go back to main menu")
                choice2 = eval(input("\t\t\tEnter your choice(1/2/3/4):-"))
                if choice2 == 1:
                    add_movies()
                elif choice2 == 2:
                    remove_movies()
                elif choice2 == 3:
                    edit_timings()
                elif choice2 == 4:
                    main()
                else:
                    print("Invalid input")
        else:
            print("Wrong Password.")
            print("1-> Try again")
            print("2-> Go back to Main menu")
            choice = eval(input("Enter your choice:-"))
            if choice == 2:
                print("Proceding back to main menu...")
                main()


def add_movies():
    if len(Movies) < 5:
        cont = "y"  # do you want to continue variable
        while cont == "y":
            mov_name = input("Enter the name of the movie to be added:-")
            mov_name = mov_name.upper()
            mov_length = eval(input("Enter the length of the movie(in minutes):-"))
            mov_screeen = eval(input("Enter the screen in which the movie shall be shown (1/2/3/4/5):-"))
            valid = 1
            while valid == 1:
                if mov_screeen in range(1, 6):
                    for i in Movies:
                        if mov_screeen == Movies[i][1]:
                            print("Screen already in use. Please choose another one.")
                            mov_screeen = eval(
                                input("Enter the screen in which the movie shall be shown (1/2/3/4/5):-"))
                            break
                    else:
                        valid = 2  # for empty Movies={}
                else:
                    print("Invalid Screen no.")
                    mov_screeen = input("Enter the screen in which the movie shall be shown (1/2/3/4/5):-")
            valid_ns = 1
            while valid_ns == 1:
                number_shows = eval(input("Enter the no. of Shows for this screen per day:-"))
                if number_shows < 1440 / (mov_length + 15):
                    valid_ns = 2
                else:
                    print("Too many shows in a single day. Please re-enter the no. of shows")
            timings = list(range(number_shows))
            for i in range(number_shows):
                validT = 1
                while validT == 1:
                    timings[i] = input("Enter the timing for the show(HH:MM):-")
                    if len(timings[i]) == 5:
                        if int(timings[i][:2]) < 24:
                            if int(timings[i][3:]) < 60:
                                validT = 2
                    else:
                        print("Invalid Timing")
            valid = 1
            while valid != 0:
                valid = 0
                for i in range(1, number_shows):
                    if (int(timings[i][:2]) - int(timings[i - 1][:2])) * 60 + int(timings[i][3:]) - int(
                            timings[i - 1][3:]) < mov_length + 15:
                        print("Time span between ", timings[i - 1], "and", timings[i],
                              "is not enough(There has to be a minimum time difference of", mov_length + 15,
                              "). Please choose another timing instead of")
                        print("1->", timings[i - 1])
                        print("2->", timings[i])
                        valid1 = 1
                        while valid1 == 1:

                            ch = eval(input("Which timing do you want to change(1/2)-"))
                            if ch == 1:
                                timings[i - 1] = input("Enter the timing for the show(HH:MM):-")
                                valid += 1
                                valid1 = 2
                            elif ch == 2:
                                timings[i] = input("Enter the timing for the show(HH:MM):-")
                                valid += 1
                                valid1 = 2
                            else:
                                print("Invalid Choice")

            validD = 1
            while validD == 1:
                start_date = input("Enter the date from which the movie will run(dd/mm/yyyy):-")
                if len(start_date) == 10:
                    if int(start_date[:2]) in range(1, 32):
                        if int(start_date[3:5]) in range(1, 13):
                            validD = 2
                        else:
                            print("Invalid date.")
                    else:
                        print("Invalid date.")
                else:
                    print("Invalid date.")

            mov_dates = list(range(7))
            for i in range(7):
                next_day = int(start_date[:2]) + i
                if int(start_date[3:5]) in [1, 3, 5, 7, 8, 10]:
                    if next_day > 31:
                        next_month = int(start_date[3:5]) + 1
                        next_day -= 31
                        if len(str(next_month)) == 1:
                            next_day = str(next_day) + "/" + "0" + str(next_month) + start_date[5:]
                        else:
                            next_day = str(next_day) + "/" + str(next_month) + start_date[5:]
                    else:
                        next_day = str(next_day) + start_date[2:]
                elif int(start_date[3:5]) in [4, 6, 9, 11]:
                    if next_day > 30:
                        next_month = int(start_date[3:5]) + 1
                        next_day -= 30
                        if len(str(next_month)) == 1:
                            next_day = str(next_day) + "/" + "0" + str(next_month) + start_date[5:]
                        else:
                            next_day = str(next_day) + "/" + str(next_month) + start_date[5:]
                    else:
                        next_day = str(next_day) + start_date[2:]
                elif int(start_date[3:5]) == 2:
                    if next_day > 28:
                        next_month = int(start_date[3:5]) + 1
                        next_day -= 28

                        next_day = str(next_day) + "/" + "0" + str(next_month) + start_date[5:]
                    else:
                        next_day = str(next_day) + start_date[2:]
                elif int(start_date[3:5]) == 12:
                    if next_day > 31:
                        next_month = 1
                        next_day -= 31
                        next_year = int(start_date[6:]) + 1
                        next_day = str(next_day) + "/" + "0" + str(next_month) + '/' + str(next_year)
                    else:
                        next_day = str(next_day) + start_date[2:]
                mov_dates[i] = next_day
            mov_dets = [mov_length, mov_screeen, number_shows, timings, mov_dates]
            Movies[mov_name] = mov_dets
            Seats = list(range(124))
            k = 1
            for j in range(124):
                Seats[j] = [k, False]
                k += 1
            Timings = {}
            for j in timings:
                Timings[j] = Seats
            Dates = {}
            for j in mov_dates:
                Dates[j] = Timings
            MoviesB[mov_name] = Dates
            if len(Movies) == 5:
                cont = 'n'
                print("No more Screens available. Proceeding back to menu......")
            else:
                cont = input("Do you want to add more movies(y/n):-")
    else:
        print("No more Screens available. Proceeding back to menu......")


def remove_movies():
    if Movies != {}:
        cont1 = "y"
        while cont1 == "y":
            print("The currently showing movies are:-")
            for i in Movies:
                print(i)
            print("Do you want to:-")
            print("1-> Proceed to remove movies")
            print("2-> Go back to Admin menu")
            choice = eval(input("Enter your choice(1/2):-"))
            if choice == 1:
                mov_name_remov = input("Enter the name of the movie to be Removed:-")
                mov_name_remov = mov_name_remov.upper()
                print("Are you sure you want to delete", mov_name_remov, "from the movie list?")
                print("1-> Yes")

                print("2-> No")
                choice1 = eval(input("Enter your choice(1/2):-"))
                if choice1 == 1:
                    del Movies[mov_name_remov]
                    del MoviesB[mov_name_remov]
                    print()
                    mov_name_remov, "has been removed"
                    print("Now the currently showing movies are:-")
                    for i in Movies:
                        print(i)
                else:
                    print('Movie not deleted')
                if len(Movies) == 0:
                    cont1 = 'n'
                    print("No more movies to be removed. Proceding back to menu.......")
                else:
                    cont1 = eval(input("Do you want to remove more movies(y/n):-"))
            elif choice == 2:
                print("Proceding back to Admin menu...")
                cont1 = 'n'
    else:
        print("No movies available. Proceding back to Admin menu.....")


def edit_timings():
    if Movies != {}:
        cont2 = "y"
        while cont2 == "y":
            print("The current movie timings are:-")
            for i in Movies:
                print(i, "\t", end=' ')
                for j in range(len(Movies[i][3])):
                    print(Movies[i][3][j], "\t", end=' ')
            print("1-> Add timings")
            print("2-> Edit timings")
            print("3-> Go back to Admin menu")
            choice = eval(input("Enter your choice(1/2/3):-"))
            Seats = list(range(124))
            k = 1
            for j in range(124):
                Seats[j] = [k, False]
                k += 1
            if choice == 1:
                no_shows_add = eval(input("Enter the no. of show timings to be added :-"))
                for i in range(no_shows_add):
                    valid_mov = 1
                    while valid_mov == 1:
                        mov_add_date = input("Enter the name of the movie whose timings are to be added :-")
                        mov_add_date = mov_add_date.upper()
                        for mov in MoviesB:

                            if mov == mov_add_date:
                                valid_mov = 2
                            else:

                                print("Invalid Movie")
                    new_timing = input("Enter the new timing for the show(HH/MM):-")
                    Movies[mov_add_date][3].append(new_timing)
                    for j in MoviesB[mov_add_date]:
                        MoviesB[mov_add_date][j][new_timing] = Seats
                    print("The new timing", new_timing, "has been added for the movie,", mov_add_date)
            elif choice == 2:
                no_shows_edit = eval(input("Enter the no. of show timings to be edited :-"))
                for i in range(no_shows_edit):
                    mov_edit_date = input("Enter the name of the movie whose timings are to be edited :-")
                    mov_edit_date = mov_edit_date.upper()
                    show_edit = input("Which show's timings are to be edited(Enter the show no.):- ")
                    not_valid = 1
                    for d in MoviesB[mov_edit_date]:
                        for s in range(124):
                            if MoviesB[mov_edit_date][Movies[mov_edit_date][3][show_edit - 1]][s][1] == True:
                                not_valid = 2
                                break
                        if not_valid == 2:
                            print("Timing not available for editing")
                            break
                    else:
                        del MoviesB[mov_edit_date][Movies[mov_edit_date][4][0]][Movies[mov_edit_date][3][show_edit - 1]]
                        print()
                        MoviesB[mov_edit_date]
                        Movies[mov_edit_date][3][show_edit - 1] = eval(
                            input("Enter the new timing for the show(HH/MM):-"))
                        for j in MoviesB[mov_edit_date]:
                            MoviesB[mov_edit_date][j][Movies[mov_edit_date][3][show_edit - 1]] = Seats
            elif choice == 3:
                print("Proceeding back to Admin menu .....")
                cont2 = 'n'
            else:
                print("Invalid choice")
                cont2 = eval(input("Do you want to continue editing timings(y/n):-"))
            if choice in [1, 2]:
                print("Now the current movie timings are:-")
                for i in Movies:
                    print(i, "\t", end=' ')
                    for j in range(len(Movies[i][3])):
                        print()
                        Movies[i][3][j], "\t",
                    print()
                cont2 = input("Do you want to continue editing timings(y/n):-")
    else:
        print("No movies available. Proceding back to Admin menu.....")


def client():
    while True:
        Password = input("Enter Your Password:-")
        if Password == "user":
            while True:
                if Movies != {}:
                    while True:
                        print("\n\t\t\t -------Client Menu-------")
                        print("\t\t_________________________________________")
                        print("\t\t\t1-> View movies")
                        print("\t\t\t2-> Make a movie reservation")
                        print("\t\t\t3-> View your reservation")
                        print("\t\t\t4-> Cancel your reservation")
                        print("\t\t\t5-> Go back to main menu")
                        choice2 = eval(input("\t\t\tEnter your choice(1/2/3/4):-"))
                        if choice2 == 1:
                            view_movies()
                        elif choice2 == 2:
                            make_reservation()
                        elif choice2 == 3:
                            view_reservation()
                        elif choice2 == 4:
                            cancel_reservation()
                        elif choice2 == 5:
                            main()
                        else:
                            print("Invalid input")
                else:
                    print("No movies Available. Returning to main menu .....")


def view_movies():
    print("The currently showing movies are:-")
    for i in Movies:
        print("\n")
        print(i, "\t\t Movie length(in min)-", Movies[i][0])
        print("Showing in Screen-", Movies[i][1])
        print("Available dates:")
        for j in range(7):
            print(Movies[i][4][j], "\t", end=' ')



def display_Seats_Screen(a, b, c):
    Seats_normal = [[random.random() for j in range(10)] for i in range(10)]
    Seats_vip = [[random.random() for j in range(12)] for i in range(2)]
    for i in range(10):
        for j in range(10):
            Seats_normal[i][j] = MoviesB[a][b][c][i * 10 + j]
    for i in range(2):
        for j in range(12):
            Seats_vip[i][j] = MoviesB[a][b][c][100 + i * 12 + j]
    print(" " * 39, "Screen")
    print(" " * 20, "_" * 50, "\n\n")
    for i in range(10):
        print(" " * 28, end=' ')
        for j in range(10):
            if Seats_normal[i][j][0] < 10:

                if Seats_normal[i][j][1] == False:
                    print(Seats_normal[i][j][0], "", end=' ')
                else:
                    print("B", "", end=' ')
            else:
                if Seats_normal[i][j][1] == False:
                    print(Seats_normal[i][j][0], end=' ')
                else:
                    print("B", "", end=' ')
        if i == 9:
            print(" " * 9, "Normal")
        else:
            print(" " * 10, "Normal")

    for i in range(2):
        print(" " * 20, end=' ')
        for j in range(12):
            if Seats_vip[i][j][1] == False:
                print(Seats_vip[i][j][0], end=' ')
            else:
                print("B", "", "", end=' ')
        print(" " * 10, "VIP")


def selecting_seatsN(a, b, c):
    Free_seatsN = 0
    for i in range(100):
        if MoviesB[a][b][c][i][1] == False:
            Free_seatsN += 1
    print("No. of Free seats =", Free_seatsN)
    Number_seatsN = eval(input("Enter the no. of seats you want to book:-"))
    client_seats = []
    if Number_seatsN <= Free_seatsN:
        i = 1
        while i <= Number_seatsN:
            Seat_number = eval(input("Enter your preferred seat no.:-"))
            if Seat_number in range(1, 101):
                if MoviesB[a][b][c][Seat_number - 1][1] == False:
                    MoviesB[a][b][c][Seat_number - 1][1] = True
                    client_seats.append(Seat_number)
                    i += 1
                elif MoviesB[a][b][c][Seat_number - 1][1] == True:
                    print("Seat is already reserved. Please choose another one.")
            else:
                print("Invalid seat no. Please choose another one.")
        timing = [2]
        client_det = [Number_seatsN, client_seats, a, b, c]
        return client_det
    else:
        print("For the selected timing this no. of seats are not available. Please choose another timing")


def selecting_seatsV(a, b, c):
    Free_seatsV = 0
    for i in range(100, 124):
        if MoviesB[a][b][c][i][1] == False:
            Free_seatsV += 1
    print("No. of Free seats =", Free_seatsV)
    Number_seatsV = eval(input("Enter the no. of seats you want to book:-"))
    client_seats = []
    if Number_seatsV <= Free_seatsV:
        i = 1
        while i <= Number_seatsV:
            Seat_number = eval(input("Enter your preferred seat no.:-"))
            if Seat_number in range(101, 125):
                if MoviesB[a][b][c][Seat_number - 1][1] == False:
                    MoviesB[a][b][c][Seat_number - 1][1] = True
                    client_seats.append(Seat_number)
                    i += 1
                elif MoviesB[a][b][c][Seat_number - 1][1] == True:
                    print("Seat is already reserved. Please choose another one.")
            else:
                print("Invalid seat no. Please choose another one.")
        timing = [2]
        client_det = [Number_seatsV, client_seats, a, b, c]
        return client_det
    else:
        print("For the selected timing this no. of seats are not available. Please choose another timing")


def make_reservation():
    print("The currently showing movies are:-")
    for i in Movies:
        print(i)
    validM = 1
    while validM == 1:
        movie_reserve = input("Enter the movie that you want to watch:-")
        for i in MoviesB:
            if movie_reserve.upper() == i:
                print("Do you want to:-")
                print("1-> Procced to select dates")
                print("2-> Go back to select movies")
                print("3-> Go back to Client menu")
                choice1 = eval(input("Enter your choice:- "))
                if choice1 == 1:
                    validM = 2
                    validD = 1
                    while validD == 1:
                        print("Selecting Dates")
                        print("\n")
                        print("The available dates for the movie are:- ")
                        for j in Movies[i][4]:
                            print(j, "\t", end=' ')

                        print("\n")
                        mov_res_date = input("On which date would you like to make the booking(dd/mm/yyyy):- ")
                        for j in MoviesB[i]:

                            if mov_res_date == j:
                                print("Do you want to:-")
                                print("1-> Procced to select timings")
                                print("2-> Go back to select dates")
                                print("3-> Go back to select Movies")
                                choice2 = eval(input("Enter your choice:- "))
                                if choice2 == 1:
                                    validD = 2
                                    validT = 1
                                    while validT == 1:
                                        print("Selecting timings")
                                        print("The available timings are:-")
                                        for k in MoviesB[i][j]:
                                            free_seats = 0
                                            for s in range(124):
                                                if MoviesB[i][j][k][s][1] == False:
                                                    free_seats += 1
                                            print(k, "\t The Available seats are", free_seats)
                                        mov_res_timing = input("Which is your show timing(HH:MM):-")
                                        for k in MoviesB[i][j]:
                                            if mov_res_timing == k:
                                                print("Do you want to:-")
                                                print("1-> Procced to select seats")
                                                print("2-> Go back to select timings ")
                                                print("3-> Go back to select Movies")
                                                choice3 = eval(input("Enter your choice:- "))
                                                if choice3 == 1:
                                                    display_Seats_Screen(i, j, k)
                                                    print("Type of Seat:-")
                                                    print("\t 1-> Normal [AED 30]")
                                                    print("\t 2-> VIP [AED 45]")
                                                    Seat_type = eval(input("Enter your preferred Seat Type(1/2):-"))
                                                    if Seat_type == 1:
                                                        client_det = selecting_seatsN(i, j, k)
                                                        if client_det == None:
                                                            make_reservation()
                                                        price = client_det[0] * 30
                                                        client_det.append(price)

                                                    elif Seat_type == 2:
                                                        client_det = selecting_seatsV(i, j, k)
                                                        if client_det == None:
                                                            make_reservation()
                                                        price = client_det[0] * 45
                                                        client_det.append(price)
                                                    valid = 1

                                                    while valid == 1:
                                                        booking_id = random.randint(1000, 25000)
                                                        for b in Clients:
                                                            if b == booking_id:
                                                                break
                                                        else:
                                                            valid = 2

                                                    Clients[booking_id] = client_det
                                                    print('Booking Details........')
                                                    print("You have booked", client_det[0], "seats, for the movie ",
                                                          client_det[2], "on ", client_det[3])
                                                    print("The movie timing is ", client_det[4], "Screen No.",
                                                          Movies[i][1])
                                                    print("Your seat no.(s) are:-", end=' ')
                                                    for x in client_det[1]:
                                                        print(x, ",", end=' ')
                                                    print("\nThe total cost = ", price)
                                                    print("Your Booking refernece no. is ", booking_id,
                                                          "Payment can be made at the ticket counter and then pick-up tickets")
                                                    validT = 2
                                                    break
                                                elif choice3 == 3:
                                                    print("Proceeding to Movie selection....")
                                                    make_reservation()
                                                elif choice3 not in [1, 2, 3]:
                                                    print("Invalid Choice")
                                        else:
                                            print("Invalid Movie timing. Please choose your timing again.")
                                elif choice2 == 3:
                                    print("Proceeding to Movie selection....")
                                    make_reservation()
                                elif choice2 not in [1, 2, 3]:
                                    print("Invalid Choice")
                                break
                        else:
                            print("Invalid Movie date. Please choose another date.")
                elif choice1 == 3:
                    print("Proceeding to Client menu....")
                    client()
                elif choice1 not in [1, 2, 3]:
                    print("Invalid Choice")
                break
        else:
            print("Invalid Movie. Please choose another movie.")


def view_reservation():
    cont1 = "y"
    while cont1 == "y":

        booking_id = eval(input("Enter your Booking reference no. - "))
        for i in Clients:
            if booking_id == i:
                client_det = Clients[booking_id]
                print('Booking Details........')
                print("You have booked", client_det[0], "seats, for the movie ", client_det[2], "on ", client_det[3])

                print("The movie timing is ", client_det[4], "Screen No.", Movies[client_det[2].upper()][1])
                print("Your seat no.(s) are:-", end=' ')
                for x in client_det[1]:
                    print(x, ",", end=' ')
                print("\n The total cost = ", client_det[5])
                break
        else:
            print("Invalid Booking reference no.")
        cont1 = input("Do you want to view another reservation(y/n):-")


def cancel_reservation():
    cont1 = "y"
    while cont1 == "y":
        booking_id = eval(input("Enter your Booking reference no. - "))
        for i in Clients:
            if booking_id == i:
                client_det = Clients[booking_id]
                del (Clients[booking_id])
                for x in range(client_det[0]):
                    MoviesB[client_det[2]][client_det[3]][client_det[4]][x - 1][1] = False
                break
        else:
            print("Invalid Booking reference no. ")
        cont1 = input("Do you want to cancel another reservation(y/n):-")


Movies = {}
MoviesB = {}
Clients = {}
main()

