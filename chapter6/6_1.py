def print_song(animal, sound):
  lyrics = "Old MacDonald had a farm, Ee-igh, Ee-igh, Oh! \n"
  lyrics = lyrics + "And on that farm he had a " + animal + " , Ee-igh, Ee-igh, Oh! \n"
  lyrics = lyrics + "With a " + sound +", "+sound + " here and a " +sound+ ", " + sound + " there. \n"
  lyrics = lyrics + "Here a " + sound + ", there a " + sound + ", everywhere a " + sound + ", " + sound + ". \n"
  lyrics = lyrics + "Old MacDonald had a farm, Ee-igh, Ee-igh, Oh! \n" 
  return lyrics

print(print_song("cow","moo"))
print(print_song("pig","oink"))
print(print_song("duck","quack"))
print(print_song("horse","neigh"))
print(print_song("lamb","baa"))

