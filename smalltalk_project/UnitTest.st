!CounterTest methodsFor: 'tests'!

testInitialValueIsZero
    self assert: counter value equals: 0.
!

testIncrementIncreasesValueByOne
    counter increment.
    self assert: counter value equals: 1.
!

testDecrementDecreasesValueByOne
    counter increment.  "So we don't go negative"
    counter decrement.
    self assert: counter value equals: 0.
!

testResetSetsValueToZero
    counter increment.
    counter increment.
    counter reset.
    self assert: counter value equals: 0.
!

testMultipleIncrements
    5 timesRepeat: [ counter increment ].
    self assert: counter value equals: 5.
!

testMultipleDecrements
    3 timesRepeat: [ counter increment ].
    2 timesRepeat: [ counter decrement ].
    self assert: counter value equals: 1.
!

