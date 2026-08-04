import { Music4 } from "lucide-react";

function FloatingLogo() {
  return (
    <div className="animate-bounce">

      <div
        className="
          mx-auto
          flex
          h-20
          w-20
          items-center
          justify-center
          rounded-full
          border
          border-green-400/20
          bg-green-500/10
          text-green-400
          backdrop-blur-xl
          shadow-[0_0_40px_rgba(34,197,94,.25)]
        "
      >
        <Music4 size={42} strokeWidth={1.6} />
      </div>

    </div>
  );
}

export default FloatingLogo;