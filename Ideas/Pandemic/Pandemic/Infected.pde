class Infected extends Person {
  int infectRadius = 75;
  int timeUntilHealthy = 60 * 7;
  
  Infected(int x, int y) {
    super(x, y, new int[] {204, 0, 0});
  }
  
  void display() {
    fill(this._color[0], this._color[1], this._color[2]);
    circle(this.x, this.y, 20);
    
    noFill();
    circle(this.x, this.y, infectRadius * 2);
  }
  
  void update(ArrayList<Person> people) {
    // Infect other people
    for (Person person : people) {
      boolean isPersonInfected = !(person instanceof Healthy) && person instanceof Infected;
      if (person == this || isPersonInfected) continue;
      
      Healthy healthyPerson = (Healthy) person;
      float distance = dist(healthyPerson.x, healthyPerson.y, this.x, this.y);
      
      if (distance <= infectRadius) {
        healthyPerson.timeInInfectRadius += 1;
      }
    }
    
    // Recover
    timeUntilHealthy--;
    if (timeUntilHealthy <= 0) {
      Healthy healthy = new Healthy(this.x, this.y);
      people.set(people.indexOf(this), healthy);
    }
  }
}
