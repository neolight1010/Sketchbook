import processing.core.*; 
import processing.data.*; 
import processing.event.*; 
import processing.opengl.*; 

import java.util.Arrays; 

import java.util.HashMap; 
import java.util.ArrayList; 
import java.io.File; 
import java.io.BufferedReader; 
import java.io.PrintWriter; 
import java.io.InputStream; 
import java.io.OutputStream; 
import java.io.IOException; 

public class ProcessingOverview extends PApplet {



int[][] savedLines = {};

public void setup() {
    
    stroke(255);
}

public void draw() {
    background(192, 64, 0);

    for (int[] line : savedLines) {
        // Draw saved lines
        line(width/2, height/2, line[0], line[1]);
    }

    line(width/2, height/2, mouseX, mouseY);
}

public int[][] appendToArray(int[][] originalArr, int[] toAppend) {
    int[][] tempArray = Arrays.copyOf(originalArr, originalArr.length + 1);
    tempArray[tempArray.length - 1] = toAppend;

    return tempArray;
}

public void mousePressed() {
    savedLines = appendToArray(savedLines, new int[] {mouseX, mouseY});;
}
  public void settings() {  size(620, 480, P2D); }
  static public void main(String[] passedArgs) {
    String[] appletArgs = new String[] { "ProcessingOverview" };
    if (passedArgs != null) {
      PApplet.main(concat(appletArgs, passedArgs));
    } else {
      PApplet.main(appletArgs);
    }
  }
}
