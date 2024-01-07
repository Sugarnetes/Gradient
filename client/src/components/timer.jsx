import React, { useState, useEffect } from 'react';
import './timer.css';

const Timer = () => {
    const [seconds, setSeconds] = useState(0);
    const [isTimerActive, setIsActive] = useState(false);
    const [timeSelected, setTimeSelected] = useState(0);

    const name = (window.location.href).split('#')[1];

    const toggle = () => {
        if (seconds === 0) {
            window.alert("Please select a time before starting the timer.");
            return;
        }
        setIsActive(!isTimerActive);
    }

    const reset = () => {
        if (!isTimerActive || window.confirm("Are you sure you want to stop the timer?")) { //timer is not active or user confirms
            setIsActive(false);
            setSeconds(0);
            setTimeSelected(0);
        }
    }

    const setTime = (minutes) => {
        if (isTimerActive) {
            window.alert("Please End the timer before changing the time.");
            return;
        }
        setSeconds(minutes * 60);
        setTimeSelected(minutes);
    }

    const complete = () => {
        setSeconds(0);
        setIsActive(false);
        if (isTimerActive) {
            window.alert(`Time's up! You have completed a ${timeSelected} minute session. Take a break!`);
        }

        /**
         * TODO: send the timer score over to the backend
         */

        const data = {
            username: name,
            timeCompleted: timeSelected,
        };

        
    }

    useEffect(() => {
        let interval = null;
        if (isTimerActive && seconds > 0) {
            interval = setInterval(() => {
                setSeconds(seconds => seconds - 1);
            }, 1000);
        } else if (isTimerActive && seconds === 0) {
            complete();
        }

        return () => clearInterval(interval);
    }, [isTimerActive, seconds]);

    const formatTime = () => {
        const minutes = Math.floor(seconds / 60);
        const remainingSeconds = seconds % 60;
        return `${String(minutes).padStart(2, '0')}:${String(remainingSeconds).padStart(2, '0')}`;
    }

    return (
        <>
            <div className="timer">
                <div className="time">
                    {formatTime()}
                </div>
                <div className="buttons">
                    <button onClick={() => setTime(25)}>25 min</button>
                    <button onClick={() => setTime(50)}>50 min</button>
                    <button onClick={toggle}>
                        {isTimerActive ? 'Pause' : 'Start'}
                    </button>
                    <button onClick={reset}>End</button>
                </div>
            </div>
        </>
    );
};

/* Debug code for timer, add under button
            <div>
                <p>Time selected: {timeSelected} minutes</p>
                <p>Timer Active: {isTimerActive ? 'Yes' : 'No'}</p> 
                </div>
*/

export default Timer;
