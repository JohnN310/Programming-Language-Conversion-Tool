// model.Counter.java
/*
 * Source: Smalltalk 'Counter' class - Chapter 1: Core Counter Logic (Model)
 * Purpose: Defines the fundamental data model and business logic for a simple numeric counter.
 */
package model;

public class Counter {
    // Instance variable: Stores the current integer value of the counter.
    private int count;

    /*
     * Method: initialize
     * Purpose: Initializes the count instance variable to 0 when a new Counter object is created.
     */
    public Counter() {
        // Calls super() implicitly, equivalent to Smalltalk's 'super initialize'.
        // 'Object's 'initialize' in Smalltalk is a no-op, so 'super()' is functionally equivalent here.
        this.count = 0;
    }

    /*
     * Method: increment
     * Purpose: Increases the count by 1.
     * Workflow: count := count + 1.
     */
    public void increment() {
        count++; // Smalltalk: count := count + 1.
    }

    /*
     * Method: decrement
     * Purpose: Decreases the count by 1.
     * Workflow: count := count - 1.
     */
    public void decrement() {
        count--; // Smalltalk: count := count - 1.
    }

    /*
     * Method: reset
     * Purpose: Resets the count to 0.
     * Workflow: count := 0.
     */
    public void reset() {
        count = 0; // Smalltalk: count := 0.
    }

    /*
     * Method: value
     * Purpose: Returns the current value of count.
     * Workflow: ^ count.
     */
    public int getValue() {
        return count; // Smalltalk: ^ count.
    }
}

// ui.CounterUI.java
/*
 * Source: Smalltalk 'Counter openUI' method - Chapter 2: User Interface (UI) Module
 * Purpose: Constructs, lays out, and displays the interactive counter UI window.
 * Design Improvement: Replaced Smalltalk's direct positioning (null layout) with Java Swing's BoxLayout
 *                     for better maintainability, responsiveness, and adaptability.
 */
package ui;

import model.Counter;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionListener;

public class CounterUI {
    private Counter counterModel; // The Counter model instance.
    private JLabel counterLabel;  // Displays the current numeric value of the counter.
    private JFrame frame;         // The main application window.

    /*
     * Constructor for CounterUI.
     * Initializes the UI components and links them to the Counter model.
     */
    public CounterUI(Counter model) {
        this.counterModel = model;
        initializeUI();
    }

    private void initializeUI() {
        // Smalltalk: window := Morph new extent: 200 @ 150; color: Color white; borderWidth: 1; borderColor: Color black.
        frame = new JFrame("My Counter App");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(200, 200); // Set initial window size similar to Smalltalk's 'extent'
        // Setting background color. Border will be handled by a JPanel.
        frame.getContentPane().setBackground(Color.WHITE);

        // Use a JPanel with BoxLayout for content organization
        // This replaces the explicit positioning (null layout) in Smalltalk.
        JPanel mainPanel = new JPanel();
        mainPanel.setLayout(new BoxLayout(mainPanel, BoxLayout.Y_AXIS)); // Vertical stacking
        mainPanel.setBorder(BorderFactory.createLineBorder(Color.BLACK)); // Mimic 'borderWidth' and 'borderColor'
        mainPanel.setBackground(Color.WHITE); // Ensure panel background is white

        // Smalltalk: counterLabel := StringMorph new contents: '0'; color: Color black; position: 100 @ 50.
        counterLabel = new JLabel(String.valueOf(counterModel.getValue()));
        counterLabel.setForeground(Color.BLACK);
        // Align label in the center horizontally
        counterLabel.setAlignmentX(Component.CENTER_ALIGNMENT);
        counterLabel.setFont(new Font("SansSerif", Font.BOLD, 24)); // Make it more prominent

        // Add some spacing before the label
        mainPanel.add(Box.createVerticalStrut(20));
        mainPanel.add(counterLabel);
        mainPanel.add(Box.createVerticalStrut(20));

        // --- Buttons --- //
        // Smalltalk: incrementButton := PluggableButtonMorph new label: 'Increment'; ...
        JButton incrementButton = createButton("Increment", e -> {
            counterModel.increment();
            updateCounterLabel();
        });
        mainPanel.add(incrementButton);
        mainPanel.add(Box.createVerticalStrut(10)); // Spacing between buttons

        // Smalltalk: decrementButton := PluggableButtonMorph new label: 'Decrement'; ...
        JButton decrementButton = createButton("Decrement", e -> {
            counterModel.decrement();
            updateCounterLabel();
        });
        mainPanel.add(decrementButton);
        mainPanel.add(Box.createVerticalStrut(10)); // Spacing between buttons

        // Smalltalk: resetButton := PluggableButtonMorph new label: 'Reset'; ...
        JButton resetButton = createButton("Reset", e -> {
            counterModel.reset();
            updateCounterLabel();
        });
        mainPanel.add(resetButton);

        // Add the main panel to the frame
        frame.getContentPane().add(mainPanel);

        // Pack the frame to fit components and center it
        frame.pack();
        frame.setLocationRelativeTo(null); // Center on screen
    }

    /*
     * Helper method to create JButtons with common styling and an ActionListener.
     * Replaces repetitive button creation and action block setup in Smalltalk.
     */
    private JButton createButton(String label, ActionListener actionListener) {
        JButton button = new JButton(label);
        button.addActionListener(actionListener);
        button.setPreferredSize(new Dimension(100, 30)); // Set preferred size, similar to Smalltalk's 'extent'
        button.setMaximumSize(new Dimension(100, 30)); // Prevent expansion with BoxLayout
        button.setAlignmentX(Component.CENTER_ALIGNMENT); // Center button horizontally
        return button;
    }

    /*
     * Updates the text of the counterLabel to reflect the current value from the model.
     * Smalltalk: counterLabel contents: self value asString.
     */
    private void updateCounterLabel() {
        counterLabel.setText(String.valueOf(counterModel.getValue()));
    }

    /*
     * Method: openUI equivalent (in the context of a separate UI class)
     * Purpose: Makes the UI window visible.
     * Smalltalk: window openInWorld.
     */
    public void show() {
        frame.setVisible(true);
    }
}

// Main.java
/*
 * Source: Smalltalk 'Test code' and 'System Integration' (implied) - Chapter 3
 * Purpose: Entry point for the Java application. Initializes the Counter model and opens its UI.
 *          The Smalltalk package cleanup mechanism has no direct Java equivalent in this context.
 */

import model.Counter;
import ui.CounterUI;

import javax.swing.SwingUtilities;

public class Main {

    public static void main(String[] args) {
        // Smalltalk: Counter new openUI

        // Create the Counter model instance
        Counter counter = new Counter();

        // Create the UI instance, passing the model
        CounterUI counterUI = new CounterUI(counter);

        // Display the UI window
        // This is done on the Event Dispatch Thread (EDT) for Swing applications
        SwingUtilities.invokeLater(() -> {
            counterUI.show();
        });

        // Smalltalk: Smalltalk at: #MyCounterApp ifPresent: [:p | p removeFromSystem].
        // This Smalltalk code snippet handles dynamic package removal and system cleanup.
        // There is no direct, equivalent translation needed or applicable in a typical Java standalone application's lifecycle.
        // Java applications are usually compiled and run from a main method, and package management is handled by the build system (e.g., Maven, Gradle).
    }
}

