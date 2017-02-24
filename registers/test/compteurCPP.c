int sleep( int t );

int main() {
  int i;
  for ( i = 0; i < 1000; i = i+1 ) {
    printd(i);
    printf("\n");
    sleep(1);
  }
  return 0;
}
