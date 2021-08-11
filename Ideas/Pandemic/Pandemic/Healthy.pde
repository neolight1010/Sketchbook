class Healthy extends Person {
  int timeInInfectRadius = 0;
  int infectThreshold = 200;
  
  Healthy(int x, int y) {
    super(x, y, new int[] {0, 255, 153});
  }
  
  void display() {
    fill(this._color[0], this._color[1], this._color[2]);
    circle(this.x, this.y, 20);
  }
  
  void update(ArrayList<Person> people) {
    if (timeInInfectRadius > infectThreshold) {
      Infected infected = new Infected(this.x, this.y);
      
      people.set(people.indexOf(this), infected);
    }
  }
}
