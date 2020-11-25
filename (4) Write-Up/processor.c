void processor(int inst,unsigned int arg)
{
   if (inst == 0)
      reg[arg] = reg[0]; //mov reg[arg], reg[0]
   else if (inst == 1)
      reg[0] -= reg[arg]; // sub reg[0], reg[arg]
   else if (inst == 2)
      reg[0] += reg[arg]; // add reg[0], reg[arg]
   else if (inst == 3)
      reg[0] *= reg[arg]; // mul reg[0], reg[arg]
   else if (inst == 4)
      reg[0] /= reg[arg]; // div reg[0], reg[arg]
   else if (inst == 5)
      reg[0] ^= reg[arg]; // xor reg[0], reg[arg]
   else if (inst == 6)
      reg[0] &= reg[arg]; // and reg[0], reg[arg]
   else if (inst == 7)
      reg[0] |= reg[arg]; // or reg[0], reg[arg]
   else if (inst == 8)
      reg[0] = reg[0] % reg[arg]; // mod reg[0], reg[arg]
   else if (inst == 9)
      reg[0] = reg[0] != arg;
   else if (inst == 10)
      reg[0] = reg[0] == arg; // cmp reg[0], arg(const)
   else if (inst == 11)
      reg[0] = reg[0] > arg; 
   else if (inst == 12)
      reg[0] = reg[0] << arg; // shl reg[0], arg
   else if (inst == 13)
   {
      reg[4]--;
      stack[reg[4]] = reg[arg]; // push reg[arg]
   }
   else if (inst == 14)
   {
      reg[arg] = stack[reg[4]]; // pop reg[arg]
      reg[4]++;
   }
   else if (inst == 16)
      putc(arg, stdout); // putc(const)
   else if (inst == 17)
      putc(reg[arg], stdout); // putc(reg[arg])
   else if (inst == 18)
      (*(void(*)(int))reg[0])(reg[arg]); // not used.
   else if (inst == 19)
      exit(0);
   else if (inst == 20)
      reg[0] = arg; // mov reg[0], arg(const)
   else if (inst == 21)
      reg[0] = reg[arg]; // mov reg[0], reg[arg]
   else if (inst == 22)
   {
      if (!reg[0]) // reg[0] == 0
         reg[5] = arg + arg - 2; // arg jump
   }
   else if (inst == 23)
   {
      if (reg[0]) // reg[0] != 0 
         reg[5] = arg + arg - 2; // arg jump;
   }
   else if (inst == 24)
      stack[reg[1]] = reg[0]; // mov [rbp+reg[1]] , reg0
   else if (inst == 25)
   {
      reg[0] = stack[reg[1]]; // mov reg[0], [rbp+reg[1]]
   }
   else if (inst == 26)
      heap[reg[1]] = (unsigned char)reg[0]; // mov byte ptr ds:[heap+reg[1]], reg[0]
   else if (inst == 27)
      reg[0] = (unsigned char)heap[reg[1]]; // mov reg[0], byte ptr ds:[heap+reg[1]]
   else if (inst == 28)
      reg[0] = heap2[reg[1]]; // mov reg0, dword ptr ds:[heap2+reg[1]]
   else if (inst == 29)
      heap2[reg[1]] = reg[0]; // mov dword ptr ds:[heap2+reg[1]], reg0
}