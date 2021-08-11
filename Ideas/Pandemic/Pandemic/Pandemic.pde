ArrayList<Person> people = new ArrayList<Person>();
int population = 40;
float initialInfectedRate = 0.2;

void setup() {
  size(800, 500);

  // Generate random population
  for (int i = 0; i < population; i++) {
    boolean isInfected = random(1) < initialInfectedRate;
    int randomX = int(random(width));
    int randomY = int(random(height));

    if (isInfected) {
      Infected infected = new Infected(randomX, randomY);
      people.add(infected);
    } else {
      Healthy healthy = new Healthy(randomX, randomY);
      people.add(healthy);
    }
  }
}

void draw() {
  background(255);

  for (Person person : people) {
    person.display();
    person.move();
    person.update(people);
  }
}
