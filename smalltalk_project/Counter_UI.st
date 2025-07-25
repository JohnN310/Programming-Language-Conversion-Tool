"Instance methods for UI"
!Counter methodsFor: 'ui'!

openUI
    | window counterLabel incrementButton decrementButton resetButton |

    window := Morph new
        extent: 200 @ 150;
        color: Color white;
        borderWidth: 1;
        borderColor: Color black.

    counterLabel := StringMorph new
        contents: '0';
        color: Color black;
        position: 100 @ 50.

    incrementButton := PluggableButtonMorph new
        label: 'Increment';
        action: [ 
            self increment.
            counterLabel contents: self value asString.
        ];
        extent: 80 @ 30;
        position: 60 @ 80.

    decrementButton := PluggableButtonMorph new
        label: 'Decrement';
        action: [ 
            self decrement.
            counterLabel contents: self value asString.
        ];
        extent: 80 @ 30;
        position: 60 @ 120.

    resetButton := PluggableButtonMorph new
        label: 'Reset';
        action: [ 
            self reset.
            counterLabel contents: self value asString.
        ];
        extent: 80 @ 30;
        position: 60 @ 160.

    window addMorph: counterLabel.
    window addMorph: incrementButton.
    window addMorph: decrementButton.
    window addMorph: resetButton.

    window openInWorld.
!