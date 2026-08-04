function Waveform() {
  return (
    <div className="pointer-events-none absolute left-1/2 top-20 -translate-x-1/2 w-[90%] max-w-6xl opacity-20">

      <svg
        viewBox="0 0 1200 120"
        className="w-full waveform"
        preserveAspectRatio="none"
      >
        <path
          d="
          M0 60
          Q40 25 80 60
          T160 60
          T240 60
          T320 60
          T400 60
          T480 60
          T560 60
          T640 60
          T720 60
          T800 60
          T880 60
          T960 60
          T1040 60
          T1120 60
          T1200 60"
          fill="none"
          stroke="#22c55e"
          strokeWidth="2"
        />
      </svg>

    </div>
  );
}

export default Waveform;