type TitleProps = {
  text: string;
};

export default function Title({ text }: TitleProps) {
  return (
    <h1 className="text-center font-mono text-7xl italic font-thin text-zinc-700 opacity-90 col-span-2 row-span-2">
      {text}
    </h1>
  );
}
