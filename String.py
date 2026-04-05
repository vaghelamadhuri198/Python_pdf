#String is data type that stores a sequence of characters.

#Strings are immutable (cannot be changed after creation).

#Each character has an index (starting from 0).

#Supports operations like concatenation, slicing, etc.

#concatination

first_name = "vaghela";
last_name = "madhuri";
first_name = "madhvi";
full_name = first_name + last_name ;
print(full_name);
print(len(full_name));

#slicing
print(full_name[1:5 ]);
print(full_name[ :5 ]);
print(full_name[ 0: ]);

#negative 
print(full_name[-1: -5 ]);
print(full_name[ : -5 ]);
print(full_name[ -0 : ]);




