int main() {
  string tab;
  int i,j;
  tab = "0";
  for ( i = 1 ; i < 100 ; i = i+1 )
    tab = cat(tab,"1");
  printf(tab);
  for ( i = 2 ; i < 10 ; i = i+1 )
  for ( j = i+i; j < 100; j = j+i ) 
  printd(j);



  return 0;
}