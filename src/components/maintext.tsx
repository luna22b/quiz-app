import HomeCards from "./HomeCards";

const MainText = () => {
  return (
    <div>
      <div className="pt-25 h-150">
        <div className="font-bold flex justify-center text-6xl max-w-[75em] px-10 flex-col items-center gap-2">
          <div>Notes and Flashcards</div>
          <div className="text-[#015d67]">that Learn with You.</div>
        </div>
        <div className="flex justify-center mt-7 text-xl px-10 text-stone-600">
          Begin studying faster using AI generated flashcards upon uploading a
          document
        </div>
        <HomeCards />
      </div>
    </div>
  );
};

export default MainText;
