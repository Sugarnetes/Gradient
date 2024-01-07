import React, { useState, useEffect } from 'react';
import './timer.css';

const Timer = () => {
    const [seconds, setSeconds] = useState(0);
    const [isActive, setIsActive] = useState(false);

    let selected = ""; 

    const toggle = () => {
        setIsActive(!isActive);
    }

    const reset = () => {
        setSeconds(0);
        setIsActive(false);
    }

    const setTime = (minutes) => {
        setSeconds(minutes * 60);
    }

    useEffect(() => {
        let interval = null;
        if (isActive) {
            interval = setInterval(() => {
                setSeconds(seconds => seconds > 0 ? seconds - 1 : 0);
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
        <div className="timer">
            <div className="time">
                {formatTime()}
            </div>
            <div className="buttons">
                <button onClick={() => setTime(25)}>25 min</button>
                <button onClick={() => setTime(50)}>50 min</button>
                <button onClick={toggle}>
                    {isActive ? 'Pause' : 'Start'}
                </button>
                <button onClick={reset}>End</button>
            </div>
        </div>
    );
};

export default Timer;
