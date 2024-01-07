import React, { useState, useEffect } from 'react';
import './timer.css';

const Timer = () => {
    const [seconds, setSeconds] = useState(0);
    const [isActive, setIsActive] = useState(false);
    const [timeSelected, setTimeSelected] = useState(0);

    const toggle = () => {
        setIsActive(!isActive);
    }

    const reset = () => {
        if (isActive && window.confirm("Are you sure you want to stop the timer?")) {
            setSeconds(0);
            setIsActive(false);
            setTimeSelected(0);
        }
    }

    const setTime = (minutes) => {
        setSeconds(minutes * 60);
        setTimeSelected(minutes);
    }

    useEffect(() => {
        let interval = null;
        if (isActive) {
            interval = setInterval(() => {
                setSeconds(seconds => {
                    if (seconds > 0) {
                        return seconds - 1;
                    } else {
                        setIsActive(false);
                        setTimeSelected(time => time > 0 ? time : 0);
                        return 0;
                    }
                });
            }, 1000);
        } else if (!isActive && seconds !== 0) {
            clearInterval(interval);
        }
        return () => clearInterval(interval);
    }, [isActive, seconds]);

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
                <button onClick={() => setTime(0.1)}>25 min</button>
                <button onClick={() => setTime(50)}>50 min</button>
                <button onClick={toggle}>
                    {isActive ? 'Pause' : 'Start'}
                </button>
                <button onClick={reset}>End</button>
            </div>
        </div>
        <div>
            <p>Time selected: {timeSelected}</p>
        </div>
        </>
    );
};

export default Timer;
