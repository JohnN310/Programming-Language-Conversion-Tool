// Counter.java
package mycounterapp;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.border.LineBorder;

// "Define the Counter class"
// Object subclass: #Counter
//     instanceVariableNames: 'count'
//     classVariableNames: ''
//     package: 'MyCounterApp'.
public class Counter {
    private int count; // Maps to 'count' instance variable

    // "Instance methods for initialization"
    // !Counter methodsFor: 'initialization'!
    // initialize
    //     super initialize.
    //     count := 0.
    public Counter() {
        super(); // Call to superclass constructor, equivalent to super initialize.
        this.count = 0; // Initialize count to 0
    }

    // "Instance methods for operations"
    // !Counter methodsFor: 'operations'!
    // increment
    //     count := count + 1.
    public void increment() {
        // Business logic: Increase the count by one
        this.count = this.count + 1;
    }

    // decrement
    //     count := count - 1.
    public void decrement() {
        // Business logic: Decrease the count by one
        this.count = this.count - 1;
    }

    // reset
    //     count := 0.
    public void reset() {
        // Business logic: Reset the count to zero
        this.count = 0;
    }

    // value
    //     ^ count
    public int value() {
        // Business logic: Provide read access to the current count
        return this.count;
    }

    // "Instance methods for UI"
    // !Counter methodsFor: 'ui'!
    // openUI
    //     | window counterLabel incrementButton decrementButton resetButton |
    public void openUI() {
        // Simulating Smalltalk Morphic UI using Java Swing components

        JFrame frame = new JFrame("MyCounterApp"); // Corresponds to 'window := Morph new'
        // Simulating extent: 200 @ 150
        frame.setSize(200, 200); // Slightly larger to accommodate buttons below each other properly
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setResizable(false); // To keep the size fixed like Morph window

        // Create a JPanel to act as the main content pane and apply styling
        JPanel windowPanel = new JPanel();
        // Simulating color: Color white
        windowPanel.setBackground(Color.WHITE);
        // Simulating borderWidth: 1; borderColor: Color black.
        windowPanel.setBorder(new LineBorder(Color.BLACK, 1));
        windowPanel.setLayout(null); // Use absolute positioning like Morphic

        frame.add(windowPanel); // Add the panel to the frame

        JLabel counterLabel = new JLabel(String.valueOf(this.count)); // Corresponds to 'counterLabel := StringMorph new contents: '0''
        counterLabel.setForeground(Color.BLACK); // Corresponds to 'color: Color black'
        counterLabel.setBounds(75, 40, 50, 20); // Corresponds to 'position: 100 @ 50' (adjusted for JLabel's text centering)

        JButton incrementButton = new JButton("Increment"); // Corresponds to 'incrementButton := PluggableButtonMorph new label: 'Increment''
        // Action block for increment button
        // action: [ self increment. counterLabel contents: self value asString. ]
        incrementButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                increment(); // Call the core business logic (model update)
                // Update the UI (view update)
                counterLabel.setText(String.valueOf(value()));
            }
        });
        incrementButton.setBounds(50, 70, 100, 30); // Corresponds to 'extent: 80 @ 30; position: 60 @ 80' (adjusted size for better fit)

        JButton decrementButton = new JButton("Decrement"); // Corresponds to 'decrementButton := PluggableButtonMorph new label: 'Decrement''
        // Action block for decrement button
        // action: [ self decrement. counterLabel contents: self value asString. ]
        decrementButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                decrement(); // Call the core business logic (model update)
                // Update the UI (view update)
                counterLabel.setText(String.valueOf(value()));
            }
        });
        decrementButton.setBounds(50, 105, 100, 30); // Corresponds to 'extent: 80 @ 30; position: 60 @ 120' (adjusted size)

        JButton resetButton = new JButton("Reset"); // Corresponds to 'resetButton := PluggableButtonMorph new label: 'Reset''
        // Action block for reset button
        // action: [ self reset. counterLabel contents: self value asString. ]
        resetButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                reset(); // Call the core business logic (model update)
                // Update the UI (view update)
                counterLabel.setText(String.valueOf(value()));
            }
        });
        resetButton.setBounds(50, 140, 100, 30); // Corresponds to 'extent: 80 @ 30; position: 60 @ 160' (adjusted size)

        // Adding components to the windowPanel
        // window addMorph: counterLabel.
        // window addMorph: incrementButton.
        // window addMorph: decrementButton.
        // window addMorph: resetButton.
        windowPanel.add(counterLabel);
        windowPanel.add(incrementButton);
        windowPanel.add(decrementButton);
        windowPanel.add(resetButton);

        // window openInWorld.
        frame.setLocationRelativeTo(null); // Center the window on screen
        frame.setVisible(true); // Make the window visible
    }

    // Main method to run the application (similar to "Counter new openUI" in Smalltalk)
    public static void main(String[] args) {
        // Ensure UI updates are done on the Event Dispatch Thread
        SwingUtilities.invokeLater(new Runnable() {
            public void run() {
                Counter counterApp = new Counter();
                counterApp.openUI();
            }
        });
    }
}

