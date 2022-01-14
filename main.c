#include <stdio.h>
#include <stdint.h>
#include <stdbool.h>

struct Tape
{

    /* Turing Memory Tape */

    int8_t arr[64][2]; // Tape Array
    int8_t JP;         // Jump Pointer
    int8_t OP;         // Operation Pointer
    int8_t DP;         // Data Pointer

};

struct TuringMS2
{

    /* Turing Machine with a main/sub tape system */

    struct Tape mtape; // Main Tape
    struct Tape stape; // Sub Tape
    int8_t cache;      // Global Cache

};

int8_t get_chunk(struct Tape tape, int8_t ind, bool operation)
{

    /* Get data from index */

    int8_t a;

    if (operation) /* Checks if getting operation */
    {
        
        a = tape.arr[ind][0];

    }
    else /* Gets data from index */
    {

        a = tape.arr[ind][1];

    }

    return a;

}

