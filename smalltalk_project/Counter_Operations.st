"Instance methods for operations"
!Counter methodsFor: 'operations'!

increment
    count := count + 1.
!

decrement
    count := count - 1.
!

reset
    count := 0.
!

value
    ^ count
!