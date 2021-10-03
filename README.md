# PyStruct
PyStruct is a module that allows users to define custom structs in python that 
corralate to packed structures in the C programming language. 

## Road Map
Planned features for PyStruct are:

  - [x] basic struct definition
  - [x] nested structs
  - [x] arrays
  - [ ] fixed-sized strings (character arrays) 

## Basic Usage
PyStruct's purpose is to add a compatibility layer for communication with C 
language applications. PyStruct will allow a user to define packed C structs in 
Python and use them for serialization.

<center>
<table>
<tr>
<td>C Struct</td><td>PyStruct</td>
</tr>
<tr>
<td>

```C
// Either _Packed 
//or no padding
struct Msg {
    uint32_t field1;
    uint32_t field2;
};
```

</td>
<td>

```python
class Msg(PyStruct):
    field1 = field(u32)
    field2 = field(u32)
```

</td>
</table>
</center>

Messages serialized on either the C language struct or in PyStruct should be compatable with each other.

## Fixed-Sized Arrays

Fixed sized arrays are also supported as struct fields:

<center>
<table>
<tr>
<td>C Struct</td><td>PyStruct</td>
</tr>
<tr>
<td>

```C
// Either _Packed 
//or no padding
struct Msg {
    uint32_t field1;
    uint32_t field2[4];
};
```

</td>
<td>

```python
class Msg(PyStruct):
    field1 = field(u32)
    field2 = field(Array(u32, 4))
```

</td>
</table>
</center>

## Nested Structs

Nested struct are also featured:
<center>
<table>
<tr>
<td>C Struct</td><td>PyStruct</td>
</tr>
<tr>
<td>

```C
// Either _Packed 
//or no padding
struct inner {
    uint32_t a;
    uint32_t b;
};

struct Msg {
    uint32_t field1;
    struct inner field2; 
    struct inner field3[2];
};
```

</td>
<td>

```python
class inner(PyStruct):
    a = field(u32)
    b = field(u32)

class Msg(PyStruct):
    field1 = field(u32)
    field2 = field(inner)  # as a scalar field
    field3 = field(Array(inner, 2)) # and as array
```

</td>
</table>
</center>
