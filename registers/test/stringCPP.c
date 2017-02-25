

int main() {
  string u;
  string s;
  string t;

  s = "hello";
  t = " world\n";
  u = "bye";
  printf("hello");
  printf("hello"+"world\n");
  printf(s+"world\n");
  printf("hello"+t);
  printf(s+t);
  printf((s+u)+t);
  printf(s+(u+t));
  printf((s+s)+(t+t));
  printf(s+u+t);
  return 0;
}