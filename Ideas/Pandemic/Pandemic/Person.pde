abstract class Person {
  int x;
  int y;
  int[] _color;
  int stepsCountdown = 20;
  float angle; // In radians
  
  Person(int x, int y, int[] _color) {
    assert _color.length == 3;
    
    this.x = x;
    this.y = y;
    this._color = _color;
  }
  
  abstract void display();
  abstract void update(ArrayList<Person> people); 
  
  void move() {
    if (this.stepsCountdown <= 0) {
      this.angle = random(TWO_PI);
      this.stepsCountdown = 20;
    }
    
    this.x += round(cos(this.angle));
    this.y += round(sin(this.angle));
    
    this.stepsCountdown--;
  }
}
