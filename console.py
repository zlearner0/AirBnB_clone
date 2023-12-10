#!/usr/bin/python3
'''contains the class for the command interpreter '''

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def interpreter(arg):
    braces = re.search(r"\{(.*?)\}", arg)
    squar = re.search(r"\[(.*?)\]", arg)
    if braces is None:
        if squar is None:
            return [i.strip(",") for i in split(arg)]
        else:
            data = split(arg[:squar.span()[0]])
            result = [i.strip(",") for i in data]
            result.append(squar.group())
            return result
    else:
        data = split(arg[:braces.span()[0]])
        result = [i.strip(",") for i in data]
        result.append(braces.group())
        return result
        

class HBNBCommand(cmd.Cmd):
    '''Set the prompt attribute to "(hbnb) "'''
    prompt = "(hbnb) "

    __c_modles = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command terminates the program"""
        print()
        return True

    def emptyline(self):
        """An empty line + ENTER nothing happends"""
        pass



    def default(self, arg):
        """update response for not proper inputs"""
        my_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        result = re.search(r"\.", arg)
        if result is not None:
            input = [arg[:result.span()[0]], arg[result.span()[1]:]]
            result = re.search(r"\((.*?)\)", input[1])
            if result is not None:
                order = [input[1][:result.span()[0]], result.group()[1:-1]]
                if order[0] in my_dict.keys():
                    call = "{} {}".format(input[0], order[1])
                    return my_dict[order[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False



    

    def do_create(self, arg):
        """Create a new  object printing its id.
        """
        input = interpreter(arg)
        if len(input) == 0:
            print("** class name missing **")
        elif input[0] not in HBNBCommand.__c_modles:
            print("** class doesn't exist **")
        else:
            print(eval(input[0])().id)
            storage.save()




    def do_show(self, arg):
        """shows the string representation of object
        """
        input = interpreter(arg)
        my_dict = storage.all()
        if len(input) == 0:
            print("** class name missing **")
        elif input[0] not in HBNBCommand.__c_modles:
            print("** class doesn't exist **")
        elif len(input) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(input[0], input[1]) not in my_dict:
            print("** no instance found **")
        else:
            print(my_dict["{}.{}".format(input[0], input[1])])

    def do_destroy(self, arg):
        """delete object by its id"""
        input = interpreter(arg)
        my_dict = storage.all()
        if len(input) == 0:
            print("** class name missing **")
        elif input[0] not in HBNBCommand.__c_modles:
            print("** class doesn't exist **")
        elif len(input) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(input[0], input[1]) not in my_dict.keys():
            print("** no instance found **")
        else:
            del my_dict["{}.{}".format(input[0], input[1])]
            storage.save()

    def do_all(self, arg):
        """dispalys all class object string representation"""
        input = interpreter(arg)
        if len(input) > 0 and input[0] not in HBNBCommand.__c_modles:
            print("** class doesn't exist **")
        else:
            my_list = []
            for inst in storage.all().values():
                if len(input) > 0 and input[0] == inst.__class__.__name__:
                    my_list.append(inst.__str__())
                elif len(input) == 0:
                    my_list.append(inst.__str__())
            print(my_list)

    def do_count(self, arg):
        """instances numbers of a class"""
        input = interpreter(arg)
        num = 0
        for inst in storage.all().values():
            if input[0] == inst.__class__.__name__:
                num += 1
        print(num)

    def do_update(self, arg):
        """update an object attribute"""
        input = interpreter(arg)
        my_dict = storage.all()

        if len(input) == 0:
            print("** class name missing **")
            return False
        if input[0] not in HBNBCommand.__c_modles:
            print("** class doesn't exist **")
            return False
        if len(input) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(input[0], input[1]) not in my_dict.keys():
            print("** no instance found **")
            return False
        if len(input) == 2:
            print("** attribute name missing **")
            return False
        if len(input) == 3:
            try:
                type(eval(input[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(input) == 4:
            inst = my_dict["{}.{}".format(input[0], input[1])]
            if input[2] in inst.__class__.__dict__.keys():
                dt_type = type(inst.__class__.__dict__[input[2]])
                inst.__dict__[input[2]] = dt_type(input[3])
            else:
                inst.__dict__[input[2]] = input[3]
        elif type(eval(input[2])) == dict:
            inst = my_dict["{}.{}".format(input[0], input[1])]
            for key, val in eval(input[2]).items():
                if (key in inst.__class__.__dict__.keys() and
                        type(inst.__class__.__dict__[key]) in {str, int, float}):
                    dt_type = type(inst.__class__.__dict__[key])
                    inst.__dict__[key] = dt_type(val)
                else:
                    inst.__dict__[key] = val
        storage.save()


        


if __name__ == '__main__':
    hbnb = HBNBCommand()
    hbnb.cmdloop()

